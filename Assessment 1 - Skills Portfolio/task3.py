from tkinter import *
from tkinter import messagebox
import os #imports the tools used for working with folders and file paths.

#Here im specifiying the color palette for the userface.
NAVY = "#530050"
SIDEBAR = "#263650"
PURPLE = "#7866C8"
LIGHT = "#F2F1F8"
WHITE = "#FFFFFF"
GREY = "#777777"
BORDER = "#DDD9EA"

# Some reusable font styles
FONT_TITLE = ("Arial", 26, "bold")
FONT_SUBTITLE = ("Arial", 12)
FONT_SECTION = ("Arial", 14, "bold")
FONT_BODY = ("Arial", 12)
FONT_BUTTON = ("Arial", 11, "bold")
FONT_INPUT = ("Arial", 12)
FONT_OUTPUT = ("Consolas", 12)

folder = os.path.dirname(os.path.abspath(__file__)) # Finds the folder where this Python program is saved.
file_name = os.path.join(folder, "A1 - Resources", "studentMarks.txt") # Builds the full path to the student marks text file.

students = [] #list that will hold all student records.

def load_students(): # Defines a function that reads the saved student records from the text file.
    with open(file_name, "r") as file: # Opens the student file in read mode so its existing information can be read.
        number_of_students = int(file.readline()) # Reads the first line, which stores the no of students, and converts it to an integer.

        for line in file:  # Loops through the remaining file lines, reading one student record at a time.
            data = line.strip().split(",")  # Removes the line break and separates the student's details wherever there is a comma.

            if len(data) == 6:
                student = [ # Starts a list for the current student's details.
                    data[0], # Stores the student number as the first item in the student list etc
                    data[1], 
                    int(data[2]), # Converts coursework 1 from text into an integer.
                    int(data[3]),
                    int(data[4]),
                    int(data[5]) # Converts the exam mark from text into an integer.
                ]
                students.append(student) # Adds the completed student record to the main students list.

    file.close()

def save_students(): # Defines a function that saves all current student records into the text file.
 
    with open(file_name, "w") as file: # Opens the file in write mode, replacing its old contents with the updated records.

        file.write(str(len(students)) + "\n") #Writes the number of students on the first line of the file.

        for student in students:  # Checks every existing student record.

            line = ( # Starts building one text line containing the current student's information.
                student[0] + "," + # Adds the student number and a comma to separate it from the next value.
                student[1] + "," + # Adds the student's name and a comma.
                str(student[2]) + "," +  # Converts coursework 1 to text and adds a comma.
                str(student[3]) + "," +
                str(student[4]) + "," +
                str(student[5]) + "\n" # Converts the exam mark to text and ends the record with a new line.
            )

            file.write(line) # Writes the completed student record into the text file.

def calculate_results(student): # Defines a function that calculates the coursework total, overall total, percentage and grade.

    coursework = student[2] + student[3] + student[4]
    total = coursework + student[5]
    percentage = (total / 160) * 100

    if percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return coursework, total, percentage, grade  

def clear_page(): #removes the previous output and action widgets from the screen.

    output.delete("1.0", END) # Deletes all text in the output box, from the first character to the end.

    for widget in action_frame.winfo_children(): # Loops through all widgets
        widget.destroy()                         #and removes the old search form before displaying the update form.

def display_student(student):

    coursework, total, percentage, grade = calculate_results(student)

    output.insert(END, "\n")
    output.insert(END, "Student Number: " + student[0] + "\n")
    output.insert(END, "Name: " + student[1] + "\n")
    output.insert(END, "Coursework 1: " + str(student[2]) + "/20\n") # Displays coursework 1 and its maximum mark of 20.
    output.insert(END, "Coursework 2: " + str(student[3]) + "/20\n")
    output.insert(END, "Coursework 3: " + str(student[4]) + "/20\n")
    output.insert(END, "Exam: " + str(student[5]) + "/100\n")  # Displays the exam mark and its maximum mark of 100.
    output.insert(END, "Coursework Total: " + str(coursework) + "/60\n")
    output.insert(END, "Overall Total: " + str(total) + "/160\n")
    output.insert(END, "Percentage: " + str(round(percentage, 2)) + "%\n") # Displays the percentage rounded to two decimal places.
    output.insert(END, "Grade: " + grade + "\n")  # Displays the student's final grade.
    output.insert(END, "-" * 45 + "\n")

def display_summary():

    total_percentage = 0

    for student in students:
        coursework, total, percentage, grade = calculate_results(student)
        total_percentage = total_percentage + percentage

    if len(students) > 0:
        average = total_percentage / len(students)
    else:
        average = 0

    output.insert(END, "\nCLASS SUMMARY\n")
    output.insert(END, "=" * 45 + "\n")
    output.insert(END, "Number of students: " + str(len(students)) + "\n")
    output.insert(END, "Class average: " + str(round(average, 2)) + "%\n")


def home():

    clear_page()

    heading.config(text="Student records manager")
    subheading.config(text="Welcome to the Student Management System")

    output.insert(END, "\nSTUDENT MANAGER\n")
    output.insert(END, "=" * 45 + "\n\n")
    output.insert(END, "Number of students: " + str(len(students)) + "\n\n")
    output.insert(END, "MENU OPTIONS\n")
    output.insert(END, "-" * 45 + "\n")
    output.insert(END, "1. View all student records\n")
    output.insert(END, "2. Find an individual student\n")
    output.insert(END, "3. View highest overall mark\n")
    output.insert(END, "4. View lowest overall mark\n")
    output.insert(END, "5. Sort student records\n")
    output.insert(END, "6. Add a student record\n")
    output.insert(END, "7. Delete a student record\n")
    output.insert(END, "8. Update a student record\n")

def view_all():

    clear_page()

    heading.config(text="All Students")
    subheading.config(text="View all student records and class statistics")

    output.insert(END, "\nALL STUDENT RECORDS\n")
    output.insert(END, "=" * 45 + "\n")

    for student in students:
        display_student(student)

    display_summary()

def view_individual():

    clear_page()

    heading.config(text="Find Student")
    subheading.config(text="Search using a student number or name")

    output.insert(END, "\nEnter a student number or name in the search box.")


def find_student(search):

    for student in students:

        if (student[0].lower() == search.lower()
                or student[1].lower() == search.lower()):
            return student

    return None


def search_student():

    search = search_entry.get().strip()

    clear_page()

    if search == "":
        output.insert(END, "Please enter a student number or name.")
        return

    student = find_student(search)

    if student is not None:
        output.insert(END, "STUDENT FOUND\n")
        output.insert(END, "=" * 45 + "\n")
        display_student(student)
    else:
        output.insert(END, "No student found.")

def highest_student():

    clear_page()

    heading.config(text="Highest Mark")
    subheading.config(text="Student with the highest overall mark")

    if len(students) == 0:
        output.insert(END, "No student records available.")
        return

    highest = students[0]

    for student in students:

        coursework, total, percentage, grade = calculate_results(student)
        highest_coursework, highest_total, highest_percentage, highest_grade = calculate_results(highest)

        if total > highest_total:
            highest = student

    output.insert(END, "STUDENT WITH HIGHEST MARK\n")
    output.insert(END, "=" * 45 + "\n")
    display_student(highest)

def lowest_student():

    clear_page()

    heading.config(text="Lowest Mark")
    subheading.config(text="Student with the lowest overall mark")

    if len(students) == 0:
        output.insert(END, "No student records available.")
        return

    lowest = students[0]

    for student in students:

        coursework, total, percentage, grade = calculate_results(student)
        lowest_coursework, lowest_total, lowest_percentage, lowest_grade = calculate_results(lowest)

        if total < lowest_total:
            lowest = student

    output.insert(END, "STUDENT WITH LOWEST MARK\n")
    output.insert(END, "=" * 45 + "\n")
    display_student(lowest)


def sort_students():

    clear_page()

    heading.config(text="Sort Records")
    subheading.config(text="Sort students by their overall marks")

    output.insert(END, "Choose how you would like to sort the records.")

    def show_sorted(order):

        clear_page()

        if order == "ascending":
            sorted_students = sorted(
                students,
                key=lambda student: calculate_results(student)[1]
            )
            output.insert(END, "STUDENTS: LOWEST TO HIGHEST\n")
        else:
            sorted_students = sorted(
                students,
                key=lambda student: calculate_results(student)[1],
                reverse=True
            )
            output.insert(END, "STUDENTS: HIGHEST TO LOWEST\n")

        output.insert(END, "=" * 45 + "\n")

        for student in sorted_students:
            display_student(student)

        display_summary()

    Button(
        action_frame,
        text="Ascending Order",
        bg=PURPLE,
        fg=WHITE,
        font=FONT_BUTTON,
        padx=16,
        pady=8,
        command=lambda: show_sorted("ascending")
    ).pack(side=LEFT, padx=5)

    Button(
        action_frame,
        text="Descending Order",
        bg=NAVY,
        fg=WHITE,
        font=FONT_BUTTON,
        padx=16,
        pady=8,
        command=lambda: show_sorted("descending")
    ).pack(side=LEFT, padx=5)

def check_marks(mark1, mark2, mark3, exam):

    if not (0 <= mark1 <= 20 and 0 <= mark2 <= 20 and 0 <= mark3 <= 20):
        messagebox.showerror(
            "Error",
            "Coursework marks must be between 0 and 20."
        )
        return False

    if not (0 <= exam <= 100):
        messagebox.showerror(
            "Error",
            "Exam mark must be between 0 and 100."
        )
        return False

    return True


def add_student():

    clear_page()

    heading.config(text="Add Student")
    subheading.config(text="Enter the details of the new student")

    labels = [
        "Student Number",
        "Student Name",
        "Coursework 1",
        "Coursework 2",
        "Coursework 3",
        "Exam"
    ]

    entries = []

    for label_text in labels:

        Label(
            action_frame,
            text=label_text,
            bg=LIGHT,
            font=FONT_BODY
        ).pack(anchor="w", pady=3)

        entry = Entry(action_frame, font=FONT_INPUT, width=38, relief="solid", bd=1)
        entry.pack(anchor="w", pady=3)
        entries.append(entry)

    def submit_student():

        number = entries[0].get().strip()
        name = entries[1].get().strip()

        if number == "" or name == "":
            messagebox.showerror(
                "Error",
                "Student number and name are required."
            )
            return

        for student in students:
            if student[0] == number:
                messagebox.showerror(
                    "Error",
                    "This student number already exists."
                )
                return

        try:
            mark1 = int(entries[2].get())
            mark2 = int(entries[3].get())
            mark3 = int(entries[4].get())
            exam = int(entries[5].get())
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter valid numbers for all marks."
            )
            return

        if check_marks(mark1, mark2, mark3, exam) == False:
            return

        new_student = [number, name, mark1, mark2, mark3, exam]
        students.append(new_student)

        save_students()

        messagebox.showinfo("Success", "Student added successfully.")
        view_all()

    Button(
        action_frame,
        text="Add Student",
        bg=PURPLE,
        fg=WHITE,
        font=FONT_BUTTON,
        command=submit_student
    ).pack(anchor="w", pady=12)

def delete_student():

    clear_page()

    heading.config(text="Delete Student")
    subheading.config(text="Delete a student using their number or name")

    Label(
        action_frame,
        text="Student Number or Name",
        bg=LIGHT,
        font=FONT_BODY
    ).pack(anchor="w", pady=5)

    delete_entry = Entry(action_frame, font=FONT_INPUT, width=38, relief="solid", bd=1)
    delete_entry.pack(anchor="w", pady=5)

    def remove_student():

        search = delete_entry.get().strip()

        if search == "":
            messagebox.showerror(
                "Error",
                "Please enter a student number or name."
            )
            return

        student = find_student(search)

        if student is None:
            messagebox.showerror("Error", "Student not found.")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete " + student[1] + "?"
        )

        if confirm:
            students.remove(student)
            save_students()

            messagebox.showinfo("Success", "Student deleted successfully.")
            view_all()

    Button(
        action_frame,
        text="Delete Student",
        bg=PURPLE,
        fg=WHITE,
        font=FONT_BUTTON,
        command=remove_student
    ).pack(anchor="w", pady=12)

def update_student():

    clear_page()

    heading.config(text="Update Student")
    subheading.config(text="Search for a student and update their details")

    Label(
        action_frame,
        text="Student Number or Name",
        bg=LIGHT,
        font=FONT_BODY
    ).pack(anchor="w", pady=5)

    update_search = Entry(action_frame, font=FONT_INPUT, width=38, relief="solid", bd=1)
    update_search.pack(anchor="w", pady=5)

    def search_for_update():

        search = update_search.get().strip()
        student = find_student(search)

        if student is None:
            messagebox.showerror("Error", "Student not found.")
            return

        for widget in action_frame.winfo_children():
            widget.destroy()

        labels = [
            "Student Number",
            "Student Name",
            "Coursework 1",
            "Coursework 2",
            "Coursework 3",
            "Exam"
        ]

        entries = []

        for i in range(6):

            Label(
                action_frame,
                text=labels[i],
                bg=LIGHT,
                font=FONT_BODY
            ).pack(anchor="w", pady=3)

            entry = Entry(action_frame, font=FONT_INPUT, width=38, relief="solid", bd=1)
            entry.pack(anchor="w", pady=3)
            entry.insert(0, str(student[i]))
            entries.append(entry)

        def save_update():

            number = entries[0].get().strip()
            name = entries[1].get().strip()

            if number == "" or name == "":
                messagebox.showerror(
                    "Error",
                    "Student number and name are required."
                )
                return

            for other_student in students:
                if other_student != student and other_student[0] == number:
                    messagebox.showerror(
                        "Error",
                        "This student number already exists."
                    )
                    return

            try:
                mark1 = int(entries[2].get())
                mark2 = int(entries[3].get())
                mark3 = int(entries[4].get())
                exam = int(entries[5].get())
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Please enter valid numbers for all marks."
                )
                return

            if check_marks(mark1, mark2, mark3, exam) == False:
                return

            student[0] = number
            student[1] = name
            student[2] = mark1
            student[3] = mark2
            student[4] = mark3
            student[5] = exam

            save_students()

            messagebox.showinfo("Success", "Student updated successfully.")
            view_all()

        Button(
            action_frame,
            text="Save Changes",
            bg=PURPLE,
            fg=WHITE,
            font=FONT_BUTTON,
            command=save_update
        ).pack(anchor="w", pady=12)

    Button(
        action_frame,
        text="Find Student",
        bg=PURPLE,
        fg=WHITE,
        font=FONT_BUTTON,
        command=search_for_update
    ).pack(anchor="w", pady=12)

root = Tk()

root.title("Student Manager")
root.geometry("1180x780")
root.minsize(1050, 700)
root.config(bg=LIGHT)

load_students()

sidebar = Frame(root, bg=NAVY, width=250)
sidebar.pack(side=LEFT, fill=Y)
sidebar.pack_propagate(False)

Label(
    sidebar,
    text="STUDENT\nMANAGER",
    bg=NAVY,
    fg=WHITE,
    font=("Arial", 21, "bold"),
    justify=LEFT
).pack(anchor="w", padx=20, pady=(25, 20))


def create_button(text, command):

    button = Button(
        sidebar,
        text=text,
        bg=NAVY,
        fg="#D6D9E2",
        activebackground=PURPLE,
        activeforeground=WHITE,
        font=FONT_BODY,
        anchor="w",
        relief="flat",
        bd=0,
        padx=22,
        pady=12,
        command=command,
        cursor="hand2"
    )

    button.pack(fill=X, padx=12, pady=3)

    # Change the button colour when the mouse enters
    button.bind(
        "<Enter>",
        lambda event: button.config(bg=SIDEBAR, fg=WHITE)
    )

    # Return to the original colour when the mouse leaves
    button.bind(
        "<Leave>",
        lambda event: button.config(bg=NAVY, fg="#D6D9E2")
    )


create_button("Home", home)
create_button("All Students", view_all)
create_button("Find Student", view_individual)
create_button("Highest Mark", highest_student)
create_button("Lowest Mark", lowest_student)

Frame(sidebar, bg="#46536A", height=1).pack(
    fill=X,
    padx=20,
    pady=12
)

Label(
    sidebar,
    text="MANAGE RECORDS",
    bg=NAVY,
    fg="#929DB0",
    font=("Arial", 9, "bold")
).pack(anchor="w", padx=20, pady=(0, 5))

create_button("Sort Records", sort_students)
create_button("Add Student", add_student)
create_button("Delete Student", delete_student)
create_button("Update Student", update_student)


content = Frame(root, bg=LIGHT)
content.pack(side=RIGHT, fill=BOTH, expand=True, padx=30, pady=25)


heading = Label(
    content,
    text="Student Manager",
    bg=LIGHT,
    fg=NAVY,
    font=FONT_TITLE
)
heading.pack(anchor="w")

subheading = Label(
    content,
    text="Welcome to the Student Management System",
    bg=LIGHT,
    fg=GREY,
    font=FONT_BODY
)
subheading.pack(anchor="w", pady=(7, 20))

action_frame = Frame(content, bg=LIGHT)
action_frame.pack(fill=X, pady=5)


search_frame = Frame(content, bg=WHITE, padx=16, pady=15)
search_frame.pack(fill=X, pady=10)

search_entry = Entry(
    search_frame,
    font=FONT_INPUT,
    width=38,
    bd=1,
    relief="solid"
)
search_entry.pack(side=LEFT, padx=5)

Button(
    search_frame,
    text="Search",
    bg=PURPLE,
    fg=WHITE,
    font=FONT_BUTTON,
    relief="flat",
    padx=20,
    pady=7,
    command=search_student
).pack(side=LEFT, padx=5)

result_frame = Frame(
    content,
    bg=WHITE,
    padx=18,
    pady=18,
    highlightbackground=BORDER,
    highlightthickness=1
)
result_frame.pack(fill=BOTH, expand=True)

output = Text(
    result_frame,
    bg=WHITE,
    fg=NAVY,
    font=FONT_OUTPUT,
    wrap="word",
    bd=0,
    padx=14,
    pady=14,
    spacing1=3,
    spacing3=3
)
output.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar for viewing long student lists
scrollbar = Scrollbar(result_frame, command=output.yview)
scrollbar.pack(side=RIGHT, fill=Y)
output.config(yscrollcommand=scrollbar.set)

home()


root.mainloop()

