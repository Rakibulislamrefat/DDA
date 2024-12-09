from datetime import datetime, date
import sqlite3
from typing import List, Dict

class Person:
    def __init__(self, name: str, age: int, contact: str, address: str):
        self.name = name
        self.age = age
        self.contact = contact
        self.address = address
        self.id = None

class Student(Person):
    def __init__(self, name: str, age: int, contact: str, address: str, license_type: str):
        super().__init__(name, age, contact, address)
        self.license_type = license_type
        self.enrollment_date = datetime.now()
        self.completed_lessons = 0
        self.test_date = None
        self.payment_status = "Pending"
        self.assigned_instructor = None

class Instructor(Person):
    def __init__(self, name: str, age: int, contact: str, address: str, specialization: str):
        super().__init__(name, age, contact, address)
        self.specialization = specialization
        self.hire_date = datetime.now()
        self.rating = 0.0
        self.students: List[Student] = []
        self.available = True

class Vehicle:
    def __init__(self, model: str, reg_number: str, category: str):
        self.id = None
        self.model = model
        self.reg_number = reg_number
        self.category = category
        self.status = "Available"
        self.last_service_date = datetime.now()
        self.assigned_instructor = None

class Course:
    def __init__(self, name: str, duration: int, fee: float, description: str):
        self.id = None
        self.name = name
        self.duration = duration  # in hours
        self.fee = fee
        self.description = description
        self.requirements = []

class DipokDrivingSchool:
    def __init__(self):
        self.db = sqlite3.connect('dipok_driving_school.db')
        self.cursor = self.db.cursor()
        self.initialize_database()

    def initialize_database(self):
        """Create necessary database tables"""
        # Students table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                contact TEXT,
                address TEXT,
                license_type TEXT,
                enrollment_date TEXT,
                completed_lessons INTEGER,
                test_date TEXT,
                payment_status TEXT,
                instructor_id INTEGER
            )
        ''')

        # Instructors table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS instructors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                contact TEXT,
                address TEXT,
                specialization TEXT,
                hire_date TEXT,
                rating REAL,
                available BOOLEAN
            )
        ''')

        # Vehicles table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vehicles (
                id INTEGER PRIMARY KEY,
                model TEXT,
                reg_number TEXT UNIQUE,
                category TEXT,
                status TEXT,
                last_service_date TEXT,
                instructor_id INTEGER
            )
        ''')

        self.db.commit()

    def register_student(self, student: Student) -> int:
        """Register a new student and return student ID"""
        self.cursor.execute('''
            INSERT INTO students (name, age, contact, address, license_type, 
                                enrollment_date, completed_lessons, payment_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (student.name, student.age, student.contact, student.address,
              student.license_type, student.enrollment_date.isoformat(),
              student.completed_lessons, student.payment_status))
        self.db.commit()
        return self.cursor.lastrowid

    def add_instructor(self, instructor: Instructor) -> int:
        """Add a new instructor and return instructor ID"""
        self.cursor.execute('''
            INSERT INTO instructors (name, age, contact, address, specialization,
                                   hire_date, rating, available)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (instructor.name, instructor.age, instructor.contact, instructor.address,
              instructor.specialization, instructor.hire_date.isoformat(),
              instructor.rating, instructor.available))
        self.db.commit()
        return self.cursor.lastrowid

    def schedule_lesson(self, student_id: int, instructor_id: int, 
                       vehicle_id: int, lesson_date: datetime) -> bool:
        """Schedule a driving lesson"""
        # Check availability
        self.cursor.execute('''
            SELECT available FROM instructors WHERE id = ?
        ''', (instructor_id,))
        if not self.cursor.fetchone()[0]:
            return False

        # Schedule the lesson
        self.cursor.execute('''
            INSERT INTO lessons (student_id, instructor_id, vehicle_id, lesson_date)
            VALUES (?, ?, ?, ?)
        ''', (student_id, instructor_id, vehicle_id, lesson_date.isoformat()))
        self.db.commit()
        return True

    def update_student_progress(self, student_id: int, lessons_completed: int):
        """Update student's completed lessons"""
        self.cursor.execute('''
            UPDATE students 
            SET completed_lessons = ?
            WHERE id = ?
        ''', (lessons_completed, student_id))
        self.db.commit()

    def process_payment(self, student_id: int, amount: float, payment_type: str):
        """Process student payment"""
        self.cursor.execute('''
            UPDATE students 
            SET payment_status = 'Paid'
            WHERE id = ?
        ''', (student_id,))
        
        self.cursor.execute('''
            INSERT INTO payments (student_id, amount, payment_type, payment_date)
            VALUES (?, ?, ?, ?)
        ''', (student_id, amount, payment_type, datetime.now().isoformat()))
        self.db.commit()

    def generate_student_report(self, student_id: int) -> Dict:
        """Generate a comprehensive student report"""
        self.cursor.execute('''
            SELECT * FROM students WHERE id = ?
        ''', (student_id,))
        student_data = self.cursor.fetchone()
        
        if not student_data:
            return {"error": "Student not found"}

        return {
            "id": student_data[0],
            "name": student_data[1],
            "license_type": student_data[5],
            "enrollment_date": student_data[6],
            "completed_lessons": student_data[7],
            "test_date": student_data[8],
            "payment_status": student_data[9]
        }

    def get_available_instructors(self) -> List[Dict]:
        """Get list of available instructors"""
        self.cursor.execute('''
            SELECT id, name, specialization, rating 
            FROM instructors 
            WHERE available = 1
        ''')
        return [{"id": row[0], "name": row[1], 
                "specialization": row[2], "rating": row[3]}
                for row in self.cursor.fetchall()]

    def __del__(self):
        """Close database connection"""
        self.db.close()

# Example Usage
def main():
    school = DipokDrivingSchool()

    # Register a new student
    student = Student(
        name="John Doe",
        age=20,
        contact="123-456-7890",
        address="123 Main St",
        license_type="Car"
    )
    student_id = school.register_student(student)

    # Add a new instructor
    instructor = Instructor(
        name="Jane Smith",
        age=35,
        contact="098-765-4321",
        address="456 Oak St",
        specialization="Car"
    )
    instructor_id = school.add_instructor(instructor)

    # Schedule a lesson
    lesson_date = datetime.now()
    school.schedule_lesson(student_id, instructor_id, 1, lesson_date)

    # Update progress
    school.update_student_progress(student_id, 5)

    # Process payment
    school.process_payment(student_id, 500.0, "Credit Card")

    # Generate report
    report = school.generate_student_report(student_id)
    print("Student Report:", report)

if __name__ == "__main__":
    main()