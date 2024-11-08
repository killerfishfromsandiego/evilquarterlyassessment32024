import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# Sample SQLite database setup (for demonstration)
def setup_database():
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Create tables for each course if they do not exist (3 columns instead of 7)
    courses = ['Geography', 'Movies', 'Science', 'Music', 'Sports']
    for course in courses:
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {course} (
                question_id INTEGER PRIMARY KEY,
                question_text TEXT,
                correct_answer TEXT
            )
        ''')

    conn.commit()
    conn.close()

# Function to fetch questions from the database
def fetch_questions(course):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT question_id, question_text, correct_answer FROM {course}')
    questions = cursor.fetchall()
    conn.close()
    return questions

# Function to add a new question to the database
def add_question(course, question_text, correct_answer):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO {course} (question_text, correct_answer)
        VALUES (?, ?)
    ''', (question_text, correct_answer))
    conn.commit()
    conn.close()

# Function to remove a question by ID from the database
def remove_question(course, question_id):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {course} WHERE question_id = ?', (question_id,))
    conn.commit()
    conn.close()

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.root.geometry("600x400")  # Set a larger window size
        self.create_first_window()

    def create_first_window(self):
        # This frame will contain the labels for each course, styled like a bullet-point list
        self.first_frame = tk.Frame(self.root)
        self.first_frame.pack(pady=20)

        self.label = tk.Label(self.first_frame, text="Select a Course:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.course_labels = []  # List to keep track of the course labels
        self.course_options = ["Geography", "Movies", "Science", "Music", "Sports"]
        
        # Create a label for each course, styled like a bullet-point list
        for course in self.course_options:
            label = tk.Label(self.first_frame, text=f"• {course}", font=("Arial", 14), cursor="hand2",
                             bg="lightgray", padx=10, pady=5, anchor="w")
            label.pack(fill="x", pady=5)
            label.bind("<Button-1>", lambda event, course=course: self.start_quiz(course))  # Bind click event to start quiz
            self.course_labels.append(label)

        # Button to manage questions
        self.manage_button = tk.Button(self.first_frame, text="Manage Questions", font=("Arial", 14), command=self.manage_questions)
        self.manage_button.pack(pady=10)

    def start_quiz(self, course):
        # Destroy the first window (course selection)
        self.first_frame.destroy()
        self.root.withdraw()  # Hide the root window

        # Create the quiz window
        self.create_quiz_window(course)

    def create_quiz_window(self, course):
        # Create a new window for the quiz
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title(f"{course} Quiz")
        quiz_window.geometry("800x600")  # Larger window for quiz

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
            self.question_label.config(text=question[1])  # Show question text
            self.answer_entry.delete(0, tk.END)  # Clear the previous answer
        else:
            self.end_quiz()

    def submit_answer(self, quiz_window):
        user_answer = self.answer_entry.get().strip().lower()  # Get and format the user input (case-insensitive)
        if user_answer:
            current_question = self.questions[self.current_question_index]
            correct_answer = current_question[2].lower()  # Get correct answer

            if user_answer == correct_answer:
                self.score += 1

            # Provide feedback for the current question
            feedback = "Correct!" if user_answer == correct_answer else f"Incorrect! The correct answer was: {current_question[2].capitalize()}"
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

    def manage_questions(self):
        # Create a new window to manage questions
        manage_window = tk.Toplevel(self.root)
        manage_window.title("Manage Questions")
        manage_window.geometry("600x400")

        # Dropdown to select a course
        self.course_dropdown = tk.StringVar(manage_window)
        self.course_dropdown.set(self.course_options[0])  # Default selection
        course_menu = tk.OptionMenu(manage_window, self.course_dropdown, *self.course_options)
        course_menu.pack(pady=20)

        # Button to view questions
        view_button = tk.Button(manage_window, text="View Questions", command=self.view_questions)
        view_button.pack(pady=10)

        # Button to add a new question
        add_button = tk.Button(manage_window, text="Add New Question", command=self.add_question_window)
        add_button.pack(pady=10)

        # Button to remove a question
        remove_button = tk.Button(manage_window, text="Remove Question", command=self.remove_question_window)
        remove_button.pack(pady=10)

    def view_questions(self):
        course = self.course_dropdown.get()
        questions = fetch_questions(course)

        # Create a new window to display the current questions
        view_window = tk.Toplevel(self.root)
        view_window.title(f"Questions for {course}")
        view_window.geometry("600x400")

        if not questions:
            messagebox.showinfo("No Questions", f"No questions found for {course}.")
        else:
            text_widget = tk.Text(view_window, width=70, height=15)
            text_widget.pack(pady=20)
            for question in questions:
                text_widget.insert(tk.END, f"ID: {question[0]}, Question: {question[1]}, Answer: {question[2]}\n")

    def add_question_window(self):
        # Prompt the user for question and answer input
        course = self.course_dropdown.get()
        question_text = simpledialog.askstring("New Question", "Enter the question text:")
        correct_answer = simpledialog.askstring("New Question", "Enter the correct answer:")

        if question_text and correct_answer:
            add_question(course, question_text, correct_answer)
            messagebox.showinfo("Success", "Question added successfully.")
        else:
            messagebox.showwarning("Input Error", "Please provide both question text and the correct answer.")

    def remove_question_window(self):
        course = self.course_dropdown.get()
        questions = fetch_questions(course)

        if not questions:
            messagebox.showwarning("No Questions", "No questions available to remove.")
            return

        # Prompt user to select a question to remove
        question_ids = [str(q[0]) for q in questions]
        question_texts = [f"ID: {q[0]} - {q[1]}" for q in questions]

        question_to_remove = simpledialog.askstring("Remove Question", f"Select a question to remove:\n{chr(10).join(question_texts)}")

        if question_to_remove in question_ids:
            question_id = int(question_to_remove)
            remove_question(course, question_id)
            messagebox.showinfo("Success", "Question removed successfully.")
        else:
            messagebox.showwarning("Invalid ID", "Please select a valid question ID.")

if __name__ == "__main__":
    setup_database()  # Initialize the database with updated questions
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
