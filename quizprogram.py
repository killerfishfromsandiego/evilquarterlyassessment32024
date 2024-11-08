import tkinter as tk
from tkinter import messagebox
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

    # Add questions for each course (Note: no options, just the correct answer)
    # Geography Questions
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (1, 'What is the capital of France?', 'Paris')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (2, 'Which continent is the Sahara Desert located in?', 'Africa')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (3, 'What is the longest river in the world?', 'Nile')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (4, 'Which country is known as the Land of the Rising Sun?', 'Japan')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (5, 'What is the largest country in the world by area?', 'Russia')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (6, 'Which ocean is the largest?', 'Pacific')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (7, 'What is the name of the mountain range that includes Mount Everest?', 'Himalayas')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (8, 'What is the smallest country in the world by area?', 'Vatican City')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (9, 'What is the largest island in the world?', 'Greenland')")
    cursor.execute(f"INSERT OR IGNORE INTO Geography VALUES (10, 'Which country has the most population in the world?', 'China')")

    # Movies Questions
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (1, 'Who directed the movie Jaws?', 'Steven spielberg')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (2, 'What is the name of the fictional African country in the movie Black Panther?', 'Wakanda')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (3, 'Who played the character of Jack Dawson in Titanic?', 'Leonardo DiCaprio')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (4, 'What is the highest-grossing movie of all time?', 'Avatar')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (5, 'In which movie did the phrase May the Force be with you first appear?', 'Star Wars')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (6, 'What movie features the character of the Joker, played by Heath Ledger?', 'The Dark Knight')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (7, 'What is the name of the fictional school in Harry Potter?', 'Hogwarts')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (8, 'Who starred as the lead in the movie The Matrix?', 'Keanu Reeves')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (9, 'Which movie won the Oscar for Best Picture in 1994?', 'Forrest Gump')")
    cursor.execute(f"INSERT OR IGNORE INTO Movies VALUES (10, 'Who voiced the character of Elsa in Disneys Frozen?', 'Idina Menzel')")

    # Science Questions
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (1, 'What is the chemical symbol for water?', 'H2O')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (2, 'What is the hardest natural substance on Earth?', 'Diamond')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (3, 'Who developed the theory of relativity?', 'Albert Einstein')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (4, 'What is the most common element in the Earths crust?', 'Oxygen')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (5, 'Which planet is known as the Red Planet?', 'Mars')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (6, 'What is the speed of light in a vacuum?', '299792458 meters per second')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (7, 'What is the process by which plants make their food?', 'Photosynthesis')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (8, 'Who is credited with discovering penicillin?', 'Alexander Fleming')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (9, 'What is the largest organ in the human body?', 'Skin')")
    cursor.execute(f"INSERT OR IGNORE INTO Science VALUES (10, 'What gas do plants absorb from the atmosphere for photosynthesis?', 'Carbon dioxide')")

    # Music Questions
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (1, 'Who is known as the King of Pop?', 'Michael Jackson')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (2, 'What band was Freddie Mercury the lead singer of?', 'Queen')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (3, 'Which country is the band ABBA from?', 'Sweden')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (4, 'What is the best-selling album of all time?', 'Thriller')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (5, 'Which musical instrument has 88 keys?', 'Piano')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (6, 'Who composed the famous symphony Ode to Joy?', 'Ludwig van Beethoven')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (7, 'What was Elvis Presleys famous nickname?', 'The King')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (8, 'Who wrote the song Imagine?', 'John Lennon')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (9, 'Which female artist released the album Lemonade in 2016?', 'Beyoncé')")
    cursor.execute(f"INSERT OR IGNORE INTO Music VALUES (10, 'What is the name of the musical genre that originated in New Orleans?', 'Jazz')")

    # Sports Questions
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (1, 'What country hosted the 2016 Summer Olympics?', 'Brazil')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (2, 'Who holds the record for the most goals in World Cup history?', 'Miroslav Klose')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (3, 'In which sport would you perform a slam dunk?', 'Basketball')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (4, 'Which country won the FIFA World Cup in 2018?', 'France')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (5, 'Who is known as The Greatest of All Time in boxing?', 'Muhammad Ali')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (6, 'What team did Michael Jordan play for in the NBA?', 'Chicago Bulls')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (7, 'In which sport would you compete in the Tour de France?', 'Cycling')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (8, 'Who is considered the fastest sprinter in the world?', 'Usain Bolt')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (9, 'What is the maximum number of players on a soccer team on the field?', '11')")
    cursor.execute(f"INSERT OR IGNORE INTO Sports VALUES (10, 'Which country is the origin of the sport of cricket?', 'England')")

    conn.commit()
    conn.close()

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
        self.course_options = ["Geography", "Movies", "Science", "Music", "Sports"]
        
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
