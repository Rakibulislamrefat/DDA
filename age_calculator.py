import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry
import time

class ClassicalAgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Classical Age Calculator")
        self.root.geometry("600x700")
        self.root.configure(bg="#F0F0F0")
        
        # Set classical style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('Classical.TFrame', background='#F0F0F0')
        style.configure('Classical.TLabel', 
                       font=('Garamond', 12),
                       background='#F0F0F0')
        style.configure('Title.TLabel',
                       font=('Garamond', 24, 'bold'),
                       background='#F0F0F0')
        style.configure('Result.TLabel',
                       font=('Garamond', 16),
                       background='#FFFFFF')

        self.create_widgets()

    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, style='Classical.TFrame', padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_frame = ttk.Frame(main_frame, style='Classical.TFrame')
        title_frame.pack(pady=20)
        
        title_label = ttk.Label(title_frame, 
                              text="Classical Age Calculator",
                              style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame,
                                 text="Calculate your precise age with elegance",
                                 style='Classical.TLabel')
        subtitle_label.pack(pady=5)

        # Input section
        input_frame = ttk.Frame(main_frame, style='Classical.TFrame')
        input_frame.pack(pady=20)

        # Birth Date
        birth_label = ttk.Label(input_frame,
                              text="Date of Birth",
                              style='Classical.TLabel')
        birth_label.pack(pady=5)
        
        self.birth_date = DateEntry(input_frame,
                                  width=20,
                                  background='#1e3c72',
                                  foreground='white',
                                  borderwidth=2,
                                  font=('Garamond', 12))
        self.birth_date.pack(pady=5)

        # Current Date
        current_label = ttk.Label(input_frame,
                                text="Current Date",
                                style='Classical.TLabel')
        current_label.pack(pady=5)
        
        self.current_date = DateEntry(input_frame,
                                    width=20,
                                    background='#1e3c72',
                                    foreground='white',
                                    borderwidth=2,
                                    font=('Garamond', 12))
        self.current_date.pack(pady=5)
        self.current_date.set_date(datetime.now())

        # Calculate Button
        calculate_btn = tk.Button(input_frame,
                                text="Calculate Age",
                                command=self.calculate_age,
                                font=('Garamond', 14),
                                bg='#1e3c72',
                                fg='white',
                                padx=20,
                                pady=10,
                                relief=tk.RAISED)
        calculate_btn.pack(pady=20)

        # Results section
        self.result_frame = ttk.Frame(main_frame, style='Classical.TFrame')
        self.result_frame.pack(pady=20, fill=tk.X)

        # Create result labels
        self.years_label = ttk.Label(self.result_frame,
                                   text="0 Years",
                                   style='Result.TLabel')
        self.years_label.pack(pady=5)
        
        self.months_label = ttk.Label(self.result_frame,
                                    text="0 Months",
                                    style='Result.TLabel')
        self.months_label.pack(pady=5)
        
        self.days_label = ttk.Label(self.result_frame,
                                  text="0 Days",
                                  style='Result.TLabel')
        self.days_label.pack(pady=5)

        # Additional information section
        self.additional_frame = ttk.Frame(main_frame, style='Classical.TFrame')
        self.additional_frame.pack(pady=20, fill=tk.X)
        
        self.additional_info = ttk.Label(self.additional_frame,
                                       text="",
                                       style='Classical.TLabel',
                                       wraplength=400)
        self.additional_info.pack(pady=5)

    def calculate_age(self):
        try:
            birth_date = self.birth_date.get_date()
            current_date = self.current_date.get_date()

            if birth_date > current_date:
                messagebox.showerror("Error", "Birth date cannot be in the future!")
                return

            # Calculate the difference
            years = current_date.year - birth_date.year
            months = current_date.month - birth_date.month
            days = current_date.day - birth_date.day

            # Adjust for negative months or days
            if days < 0:
                months -= 1
                # Calculate days remaining in the month
                temp_date = current_date.replace(day=1)
                days = (temp_date - birth_date.replace(day=1)).days

            if months < 0:
                years -= 1
                months += 12

            # Animate results
            self.animate_number(self.years_label, years, "Years")
            self.animate_number(self.months_label, months, "Months")
            self.animate_number(self.days_label, days, "Days")

            # Calculate additional information
            total_days = (current_date - birth_date).days
            total_months = years * 12 + months
            total_weeks = total_days // 7

            additional_text = (
                f"You have lived for approximately:\n"
                f"{total_days:,} days\n"
                f"{total_weeks:,} weeks\n"
                f"{total_months:,} months\n"
                f"{total_days * 24:,} hours\n"
                f"{total_days * 24 * 60:,} minutes"
            )
            
            self.additional_info.configure(text=additional_text)

        except Exception as e:
            messagebox.showerror("Error", "Please enter valid dates!")

    def animate_number(self, label, final_number, suffix):
        steps = 20
        duration = 50  # milliseconds between steps
        
        def update_number(current_step):
            if current_step <= steps:
                number = int((final_number * current_step) / steps)
                label.configure(text=f"{number} {suffix}")
                self.root.after(duration, 
                              lambda: update_number(current_step + 1))
        
        update_number(1)

def main():
    root = tk.Tk()
    app = ClassicalAgeCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 