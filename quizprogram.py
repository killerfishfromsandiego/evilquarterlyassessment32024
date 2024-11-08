import tkinter as tk
from tkinter import messagebox
import sqlite3

# Sample SQLite database setup (for demonstration)
def setup_database():
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Create tables for each course if they do not exist (3 columns instead of 7)
    courses = ['ECON2020', 'DS3850', 'ECON3610', 'DS3860', 'ACCT2120']
    for course in courses:
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {course} (
                question_id INTEGER PRIMARY KEY,
                question_text TEXT,
                correct_answer TEXT
            )
        ''')

# Function to fetch questions from the database
def fetch_questions(course):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT question_text, correct_answer FROM {course}')
    questions = cursor.fetchall()
    conn.close()
    return [Question(*q) for q in questions]

class Question:
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer.lower()  # Store answers in lowercase for case-insensitivity

    def display(self):
        return self.question_text

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.root.geometry("600x400")  
        self.create_first_window()

    def create_first_window(self):
        # this frame contains the courses in a bullet point format
        self.first_frame = tk.Frame(self.root)
        self.first_frame.pack(pady=20)

        self.label = tk.Label(self.first_frame, text="Select a Course:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.course_labels = []  # list that contains the courses
        self.course_options = ["ECON2020", "DS3850", "ECON3610", "DS3860", "ACCT2120"]
        
        #creates labels in a bullet point format
        for course in self.course_options:
            label = tk.Label(self.first_frame, text=f"• {course}", font=("Arial", 14), cursor="hand2",
                             bg="lightgray", padx=10, pady=5, anchor="w")
            label.pack(fill="x", pady=5)
            label.bind("<Button-1>", lambda event, course=course: self.start_quiz(course))  #makes it so when you click the button it starts the quiz
            self.course_labels.append(label)

    def start_quiz(self, course):
        # Destroy the first window (course selection) and root window
        self.first_frame.destroy()
        self.root.withdraw()  # Hide the root window

        # Create the quiz window
        self.create_quiz_window(course)

    def create_quiz_window(self, course):
        # Create a new window for the quiz
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title(f"{course} Quiz")
        quiz_window.geometry("800x600") 

        self.questions = fetch_questions(course)
        self.current_question_index = 0
        self.score = 0

        # Set up the question display area
        self.question_label = tk.Label(quiz_window, text="", font=("Arial", 16), wraplength=750, justify="left")
        self.question_label.pack(pady=20)

        # Set up the answer entry area
        self.answer_entry = tk.Entry(quiz_window, font=("Arial", 14), width=40)
        self.answer_entry.pack(pady=10)

        # Submit button to check the answer
        self.submit_button = tk.Button(quiz_window, text="Submit Answer", command=lambda: self.submit_answer(quiz_window), font=("Arial", 14))
        self.submit_button.pack(pady=10)

        self.display_question()

        quiz_window.protocol("WM_DELETE_WINDOW", self.quit_program)

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question.display())
            self.answer_entry.delete(0, tk.END)  # Clear the previous answer
        else:
            self.end_quiz()

    def submit_answer(self, quiz_window):
        user_answer = self.answer_entry.get().strip().lower()  # Get and format the user input (case-insensitive)
        if user_answer:
            current_question = self.questions[self.current_question_index]
            if user_answer == current_question.correct_answer:
                self.score += 1

            # Provide feedback for the current question
            feedback = "Correct!" if user_answer == current_question.correct_answer else f"WRONG!! HERES THE ANSWER: {current_question.correct_answer}"
            messagebox.showinfo("Answer Feedback", feedback)

            # Move to the next question
            self.current_question_index += 1
            self.display_question()
        else:
            messagebox.showwarning("Warning", "Please enter an answer.")

    def end_quiz(self):
        total_questions = len(self.questions)
        if total_questions > 0:
            score_percentage = (self.score / total_questions) * 100
            result_text = f"Quiz Complete! Your score: {self.score}/{total_questions} ({score_percentage:.2f}%)"
        else:
            result_text = "No questions available for this quiz."

        messagebox.showinfo("Quiz Complete", result_text)
        self.quit_program()

    def quit_program(self):
        self.root.quit()  # End the program when the quiz window is closed

if __name__ == "__main__":
    setup_database()  # Initialize the database with updated questions
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
