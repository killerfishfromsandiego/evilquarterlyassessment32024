import sqlite3
from tkinter import Tk, Frame, Label, Button, OptionMenu, StringVar, messagebox, simpledialog, Toplevel, Scrollbar, Text

# Function to fetch current questions from a specific course
def fetch_questions(course):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT question_id, question_text, correct_answer FROM {course}')
    questions = cursor.fetchall()
    conn.close()
    return questions

# Function to remove a question by ID from the database
def remove_question(course, question_id):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {course} WHERE question_id = ?', (question_id,))
    conn.commit()
    conn.close()

# Function to add a question to the database
def add_question(course, question_text, correct_answer):
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {course} (question_text, correct_answer) VALUES (?, ?)', 
                   (question_text, correct_answer))
    conn.commit()
    conn.close()

# Function to handle adding a question
def add_question_interface(course, frame, question_display):
    question_text = simpledialog.askstring("Add Question", "Enter the question text:")
    correct_answer = simpledialog.askstring("Add Question", "Enter the correct answer:")

    if question_text and correct_answer:
        add_question(course, question_text, correct_answer)
        messagebox.showinfo("Success", "Question added successfully.")
    else:
        messagebox.showwarning("Input Error", "Both question text and answer must be provided.")

# Function to handle removing a question
def remove_question_interface(course, frame, question_display):
    questions = fetch_questions(course)

    if not questions:
        messagebox.showinfo("No Questions", f"There are no questions available to remove in the {course} course.")
        return

    # Create a new Toplevel window for removing a question
    top = Toplevel()
    top.title(f"Remove Question from {course}")
    top.geometry("500x300")

    # Create a Scrollbar and Text widget to show the list of questions
    scrollbar = Scrollbar(top)
    scrollbar.pack(side="right", fill="y")

    question_text_area = Text(top, wrap="word", height=10, width=50, yscrollcommand=scrollbar.set)
    question_text_area.pack(padx=20, pady=20)

    scrollbar.config(command=question_text_area.yview)

    # Function to refresh the question list
    def refresh_question_list():
        # Fetch updated questions from the database
        questions = fetch_questions(course)
        # Generate the string representation of questions to display
        question_list = "\n".join([f"ID: {q[0]} - {q[1]} (Answer: {q[2]})" for q in questions])
        # Clear the Text widget and insert the updated question list
        question_text_area.delete(1.0, "end")
        question_text_area.insert("1.0", question_list)

    # Display all questions initially
    refresh_question_list()

    # Ask for question ID to remove
    def on_remove_question():
        question_to_remove = simpledialog.askstring("Remove Question", "Enter the Question ID to remove:")

        try:
            question_to_remove = int(question_to_remove)
            question_exists = any(q[0] == question_to_remove for q in questions)
            
            if question_exists:
                remove_question(course, question_to_remove)
                messagebox.showinfo("Success", "Question removed successfully.")
                refresh_question_list()  # Refresh the list after removal
            else:
                messagebox.showerror("Invalid ID", "The selected question ID does not exist.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid question ID.")

    # Add the remove button
    Button(top, text="Ready to remove a question? CLICK ME!!!", command=on_remove_question, font=("Arial", 12)).pack(pady=10)

    # Add a Close button to close the window
    Button(top, text="Close", command=top.destroy, font=("Arial", 12)).pack(pady=10)

# Function to view questions in a new window (Toplevel)
def view_questions(course):
    questions = fetch_questions(course)

    if not questions:
        messagebox.showinfo("No Questions", f"There are no questions available for the {course} course.")
        return

    # Create a new Toplevel window
    top = Toplevel()
    top.title(f"Questions for {course}")
    top.geometry("500x300")

    # Create a Scrollbar and Text widget to show the list of questions
    scrollbar = Scrollbar(top)
    scrollbar.pack(side="right", fill="y")

    question_text_area = Text(top, wrap="word", height=10, width=50, yscrollcommand=scrollbar.set)
    question_text_area.pack(padx=20, pady=20)

    scrollbar.config(command=question_text_area.yview)

    # Display all questions
    question_list = "\n".join([f"ID: {q[0]} - {q[1]} (Answer: {q[2]})" for q in questions])
    question_text_area.insert("1.0", question_list)
    question_text_area.config(state="disabled")  # Make the text area read-only

    # Add a Close button to close the window
    Button(top, text="Close", command=top.destroy, font=("Arial", 12)).pack(pady=10)

# Update the frame to show the appropriate options based on the selected course
def update_frame(frame, course):
    # Clear the current frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Add new options
    Label(frame, text=f"Manage Questions for {course}", font=("Arial", 16), bg="#8B0000", fg="white").pack(pady=10)

    # Buttons for managing questions
    Button(frame, text="View Questions", command=lambda: view_questions(course), font=("Arial", 14), bg="white", fg="black").pack(pady=10, fill="x")
    Button(frame, text="Add Question", command=lambda: add_question_interface(course, frame, None), font=("Arial", 14), bg="white", fg="black").pack(pady=10, fill="x")
    Button(frame, text="Remove Question", command=lambda: remove_question_interface(course, frame, None), font=("Arial", 14), bg="white", fg="black").pack(pady=10, fill="x")
    
    # Add back button
    Button(frame, text="Back", command=lambda: show_course_selection(frame), font=("Arial", 14), bg="white", fg="black").pack(pady=10, fill="x")

# Show the course selection page
def show_course_selection(frame):
    # Clear the current frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Create dropdown for course selection
    course_options = ["ECON2020", "DS3850", "ECON3610", "DS3860", "ACCT2120"]
    selected_course = StringVar()
    selected_course.set(course_options[0])  # Default to the first course

    Label(frame, text="Select a Course", font=("Arial", 16), bg="#8B0000", fg="white").pack(pady=10)
    course_dropdown = OptionMenu(frame, selected_course, *course_options)
    course_dropdown.config(font=("Arial", 14), bg="white", fg="black")
    course_dropdown.pack(pady=10, fill="x")

    # Button to load course management options
    Button(frame, text="Manage Questions", command=lambda: update_frame(frame, selected_course.get()), font=("Arial", 14), bg="white", fg="black").pack(pady=10)

# Main interface to manage questions
def manage_questions_interface():
    # Set up Tkinter window
    root = Tk()
    root.title("Manage Questions")
    root.geometry("600x400")  # Window size

    # Set background color to dark red
    root.configure(bg="#8B0000")  # Dark red color

    # Create a frame for buttons and labels
    frame = Frame(root, bg="#8B0000")
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Show course selection page initially
    show_course_selection(frame)

    root.mainloop()

if __name__ == "__main__":
    manage_questions_interface()
