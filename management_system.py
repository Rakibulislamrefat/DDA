import datetime
import sqlite3
from typing import List

class Student:
    def __init__(self, name: str, age: int, contact: str, course_type: str):
        self.id = None
        self.name = name
        self.age = age
        self.contact = contact
        self.course_type = course_type
        self.enrollment_date = datetime.datetime.now()
        self.lessons_completed = 0
        self.payment_status = "Pending"

class Instructor:
    def __init__(self, name: str, specialization: str, contact: str):
        self.id = None
        self.name = name
        self.specialization = specialization
        self.contact = contact
        self.students: List[Student] = []
        self.availability = True

class Vehicle:
    def __init__(self, model: str, plate_number: str, vehicle_type: str):
        self.id = None
        self.model = model
        self.plate_number = plate_number
        self.vehicle_type = vehicle_type
        self.status = "Available"
        self.last_maintenance = datetime.datetime.now()

class Course:
    def __init__(self, name: str, duration: int, price: float):
        self.id = None
        self.name = name
        self.duration = duration  # in hours
        self.price = price
        self.lessons = []

class DrivingSchoolManagement:
    def __init__(self):
        self.db_connection = sqlite3.connect('driving_school.db')
        self.cursor = self.db_connection.cursor()
        self.create_tables()
        
    def create_tables(self):
        # Create necessary database tables
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                contact TEXT,
                course_type TEXT,
                enrollment_date TEXT,
                lessons_completed INTEGER,
                payment_status TEXT
            )
        ''')
        
        # Add other tables (instructors, vehicles, courses, etc.)
        self.db_connection.commit()

    def add_student(self, student: Student):
        self.cursor.execute('''
            INSERT INTO students (name, age, contact, course_type, enrollment_date, 
                                lessons_completed, payment_status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (student.name, student.age, student.contact, student.course_type,
              student.enrollment_date.isoformat(), student.lessons_completed,
              student.payment_status))
        self.db_connection.commit()
        return self.cursor.lastrowid

    def schedule_lesson(self, student_id: int, instructor_id: int, 
                       vehicle_id: int, date_time: datetime.datetime):
        # Implementation for scheduling lessons
        pass

    def record_payment(self, student_id: int, amount: float):
        # Implementation for recording payments
        pass

    def update_student_progress(self, student_id: int, lessons_completed: int):
        self.cursor.execute('''
            UPDATE students 
            SET lessons_completed = ?
            WHERE id = ?
        ''', (lessons_completed, student_id))
        self.db_connection.commit()

    def get_student_details(self, student_id: int) -> dict:
        self.cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        result = self.cursor.fetchone()
        if result:
            return {
                'id': result[0],
                'name': result[1],
                'age': result[2],
                'contact': result[3],
                'course_type': result[4],
                'enrollment_date': result[5],
                'lessons_completed': result[6],
                'payment_status': result[7]
            }
        return None

    def generate_progress_report(self, student_id: int) -> str:
        student = self.get_student_details(student_id)
        if student:
            report = f"""
            Progress Report for {student['name']}
            ----------------------------------------
            Course Type: {student['course_type']}
            Lessons Completed: {student['lessons_completed']}
            Enrollment Date: {student['enrollment_date']}
            Payment Status: {student['payment_status']}
            """
            return report
        return "Student not found"

# Example Usage
def main():
    # Initialize the management system
    school = DrivingSchoolManagement()

    # Add a new student
    new_student = Student(
        name="John Doe",
        age=20,
        contact="123-456-7890",
        course_type="Basic Driver's License"
    )
    student_id = school.add_student(new_student)

    # Update progress
    school.update_student_progress(student_id, 5)

    # Generate and print progress report
    print(school.generate_progress_report(student_id))

if __name__ == "__main__":
    main() 