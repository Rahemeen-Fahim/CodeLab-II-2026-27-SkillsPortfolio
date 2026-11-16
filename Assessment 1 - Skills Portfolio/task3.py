from tkinter import *
from tkinter import messagebox

NAVY = "#530050"
SIDEBAR = "#263650"
PURPLE = "#7866C8"
LIGHT = "#F2F1F8"
WHITE = "#FFFFFF"
GREY = "#777777"

students = []

file = open("studentMarks.txt", "r")

number_of_students = int(file.readline())

for line in file:
    data = line.strip().split(",")

    student = [
        data[0],
        data[1],
        int(data[2]),
        int(data[3]),
        int(data[4]),
        int(data[5])
    ]

    students.append(student)

file.close()


# ==========================================
# 3. SAVE STUDENT DATA
# ==========================================

def save_students():

    file = open("studentMarks.txt", "w")

    file.write(str(len(students)) + "\n")

    for student in students:

        line = (
            student[0] + "," +
            student[1] + "," +
            str(student[2]) + "," +
            str(student[3]) + "," +
            str(student[4]) + "," +
            str(student[5]) + "\n"
        )

        file.write(line)

    file.close()


# ==========================================
# 4. CALCULATE STUDENT RESULTS
# ==========================================

def calculate_results(student):

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


# ==========================================
# 5. CLEAR PAGE
# ==========================================

def clear_page():

    output.delete("1.0", tk.END)

    for widget in action_frame.winfo_children():
        widget.destroy()


# ==========================================
# 6. DISPLAY INDIVIDUAL STUDENT
# ==========================================

def display_student(student):

    coursework, total, percentage, grade = calculate_results(student)

    output.insert(tk.END, "\n")

    output.insert(tk.END, "Student Number: " + student[0] + "\n")
    output.insert(tk.END, "Name: " + student[1] + "\n")

    output.insert(tk.END, "Coursework 1: " + str(student[2]) + "/20\n")
    output.insert(tk.END, "Coursework 2: " + str(student[3]) + "/20\n")
    output.insert(tk.END, "Coursework 3: " + str(student[4]) + "/20\n")

    output.insert(tk.END, "Exam: " + str(student[5]) + "/100\n")

    output.insert(tk.END, "Coursework Total: " + str(coursework) + "/60\n")
    output.insert(tk.END, "Overall Total: " + str(total) + "/160\n")

    output.insert(tk.END, "Percentage: " + str(round(percentage, 2)) + "%\n")
    output.insert(tk.END, "Grade: " + grade + "\n")

    output.insert(tk.END, "-" * 45 + "\n")


# ==========================================
# 7. HOME PAGE
# ==========================================

def home():

    clear_page()

    heading.config(text="Student Manager")
    subheading.config(text="Welcome to the Student Management System")

    output.insert(tk.END, "\n")
    output.insert(tk.END, "STUDENT MANAGER\n")
    output.insert(tk.END, "=" * 45 + "\n\n")

    output.insert(tk.END, "Number of students: " + str(len(students)) + "\n\n")

    output.insert(tk.END, "MENU OPTIONS\n")
    output.insert(tk.END, "-" * 45 + "\n")

    output.insert(tk.END, "1. View all student records\n")
    output.insert(tk.END, "2. Find an individual student\n")
    output.insert(tk.END, "3. View highest overall mark\n")
    output.insert(tk.END, "4. View lowest overall mark\n")
    output.insert(tk.END, "5. Sort student records\n")
    output.insert(tk.END, "6. Add a student record\n")
    output.insert(tk.END, "7. Delete a student record\n")
    output.insert(tk.END, "8. Update a student record\n")


# ==========================================
# 8. VIEW ALL STUDENTS
# ==========================================

def view_all():

    clear_page()

    heading.config(text="All Students")
    subheading.config(text="View all student records and class statistics")

    output.insert(tk.END, "\nALL STUDENT RECORDS\n")
    output.insert(tk.END, "=" * 45 + "\n")

    total_percentage = 0

    for student in students:

        display_student(student)

        coursework, total, percentage, grade = calculate_results(student)

        total_percentage = total_percentage + percentage

    if len(students) > 0:
        average = total_percentage / len(students)
    else:
        average = 0

    output.insert(tk.END, "\nCLASS SUMMARY\n")
    output.insert(tk.END, "=" * 45 + "\n")

    output.insert(tk.END, "Number of students: " + str(len(students)) + "\n")

    output.insert(tk.END, "Class average: " + str(round(average, 2)) + "%\n")


# ==========================================
# 9. FIND STUDENT
# ==========================================

def view_individual():

    clear_page()

    heading.config(text="Find Student")
    subheading.config(text="Search using a student number or name")

    output.insert(tk.END, "\nEnter a student number or name in the search box.")


def find_student(search):

    for student in students:

        if student[0].lower() == search.lower() or student[1].lower() == search.lower():
            return student

    return None


def search_student():

    search = search_entry.get().strip()

    clear_page()

    if search == "":
        output.insert(tk.END, "Please enter a student number or name.")
        return

    student = find_student(search)

    if student is not None:

        output.insert(tk.END, "STUDENT FOUND\n")
        output.insert(tk.END, "=" * 45 + "\n")

        display_student(student)

    else:

        output.insert(tk.END, "No student found.")


# ==========================================
# 10. HIGHEST STUDENT
# ==========================================

def highest_student():

    clear_page()

    heading.config(text="Highest Mark")
    subheading.config(text="Student with the highest overall mark")

    if len(students) == 0:

        output.insert(tk.END, "No student records available.")
        return

    highest = students[0]

    for student in students:

        coursework, total, percentage, grade = calculate_results(student)

        highest_coursework, highest_total, highest_percentage, highest_grade = calculate_results(highest)

        if total > highest_total:
            highest = student

    output.insert(tk.END, "STUDENT WITH HIGHEST MARK\n")
    output.insert(tk.END, "=" * 45 + "\n")

    display_student(highest)


# ==========================================
# 11. LOWEST STUDENT
# ==========================================

def lowest_student():

    clear_page()

    heading.config(text="Lowest Mark")
    subheading.config(text="Student with the lowest overall mark")

    if len(students) == 0:

        output.insert(tk.END, "No student records available.")
        return

    lowest = students[0]

    for student in students:

        coursework, total, percentage, grade = calculate_results(student)

        lowest_coursework, lowest_total, lowest_percentage, lowest_grade = calculate_results(lowest)

        if total < lowest_total:
            lowest = student

    output.insert(tk.END, "STUDENT WITH LOWEST MARK\n")
    output.insert(tk.END, "=" * 45 + "\n")

    display_student(lowest)


# ==========================================
# 12. SORT STUDENT RECORDS
# ==========================================

def sort_students():

    clear_page()

    heading.config(text="Sort Records")
    subheading.config(text="Sort students by their overall marks")

    output.insert(tk.END, "Choose how you would like to sort the records.")

    def show_sorted(order):

        clear_page()

        if order == "ascending":

            sorted_students = sorted(
                students,
                key=lambda student: calculate_results(student)[1]
            )

            output.insert(tk.END, "STUDENTS: LOWEST TO HIGHEST\n")

        else:

            sorted_students = sorted(
                students,
                key=lambda student: calculate_results(student)[1],
                reverse=True
            )

            output.insert(tk.END, "STUDENTS: HIGHEST TO LOWEST\n")

        output.insert(tk.END, "=" * 45 + "\n")

        total_percentage = 0

        for student in sorted_students:

            display_student(student)

            coursework, total, percentage, grade = calculate_results(student)

            total_percentage = total_percentage + percentage

        if len(sorted_students) > 0:
            average = total_percentage / len(sorted_students)
        else:
            average = 0

        output.insert(tk.END, "\nCLASS SUMMARY\n")
        output.insert(tk.END, "=" * 45 + "\n")

        output.insert(tk.END, "Number of students: " + str(len(students)) + "\n")

        output.insert(tk.END, "Class average: " + str(round(average, 2)) + "%\n")

    tk.Button(
        action_frame,
        text="Ascending Order",
        bg=PURPLE,
        fg=WHITE,
        font=("Arial", 10, "bold"),
        command=lambda: show_sorted("ascending")
    ).pack(side="left", padx=5)

    tk.Button(
        action_frame,
        text="Descending Order",
        bg=NAVY,
        fg=WHITE,
        font=("Arial", 10, "bold"),
        command=lambda: show_sorted("descending")
    ).pack(side="left", padx=5)


# ==========================================
# 13. ADD STUDENT
# ==========================================

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

    for label in labels:

        tk.Label(
            action_frame,
            text=label,
            bg=LIGHT,
            font=("Arial", 10)
        ).pack(anchor="w", pady=3)

        entry = tk.Entry(
            action_frame,
            font=("Arial", 10),
            width=35
        )

        entry.pack(anchor="w", pady=3)

        entries.append(entry)

    def submit_student():

        number = entries[0].get().strip()
        name = entries[1].get().strip()

        if number == "" or name == "":
            messagebox.showerror("Error", "Student number and name are required.")
            return

        for student in students:

            if student[0] == number:
                messagebox.showerror("Error", "This student number already exists.")
                return

        try:

            mark1 = int(entries[2].get())
            mark2 = int(entries[3].get())
            mark3 = int(entries[4].get())
            exam = int(entries[5].get())

        except ValueError:

            messagebox.showerror("Error", "Please enter valid numbers for all marks.")
            return

        if not (0 <= mark1 <= 20 and 0 <= mark2 <= 20 and 0 <= mark3 <= 20):
            messagebox.showerror("Error", "Coursework marks must be between 0 and 20.")
            return

        if not (0 <= exam <= 100):
            messagebox.showerror("Error", "Exam mark must be between 0 and 100.")
            return

        new_student = [number, name, mark1, mark2, mark3, exam]

        students.append(new_student)

        save_students()

        messagebox.showinfo("Success", "Student added successfully.")

        view_all()

    tk.Button(
        action_frame,
        text="Add Student",
        bg=PURPLE,
        fg=WHITE,
        font=("Arial", 10, "bold"),
        command=submit_student
    ).pack(anchor="w", pady=12)


# ==========================================
# 14. DELETE STUDENT
# ==========================================

def delete_student():

    clear_page()

    heading.config(text="Delete Student")
    subheading.config(text="Delete a student using their number or name")

    tk.Label(
        action_frame,
        text="Student Number or Name",
        bg=LIGHT,
        font=("Arial", 10)
    ).pack(anchor="w", pady=5)

    delete_entry = tk.Entry(
        action_frame,
        font=("Arial", 10),
        width=35
    )

    delete_entry.pack(anchor="w", pady=5)

    def remove_student():

        search = delete_entry.get().strip()

        if search == "":
            messagebox.showerror("Error", "Please enter a student number or name.")
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

    tk.Button(
        action_frame,
        text="Delete Student",
        bg=PURPLE,
        fg=WHITE,
        font=("Arial", 10, "bold"),
        command=remove_student
    ).pack(anchor="w", pady=12)


# ==========================================
# 15. UPDATE STUDENT
# ==========================================

def update_student():

    clear_page()

    heading.config(text="Update Student")
    subheading.config(text="Search for a student and update their details")

    tk.Label(
        action_frame,
        text="Student Number or Name",
        bg=LIGHT,
        font=("Arial", 10)
    ).pack(anchor="w", pady=5)

    update_search = tk.Entry(
        action_frame,
        font=("Arial", 10),
        width=35
    )

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

            tk.Label(
                action_frame,
                text=labels[i],
                bg=LIGHT,
                font=("Arial", 10)
            ).pack(anchor="w", pady=3)

            entry = tk.Entry(
                action_frame,
                font=("Arial", 10),
                width=35
            )

            entry.pack(anchor="w", pady=3)

            entry.insert(0, str(student[i]))

            entries.append(entry)

        def save_update():

            number = entries[0].get().strip()
            name = entries[1].get().strip()

            if number == "" or name == "":
                messagebox.showerror("Error", "Student number and name are required.")
                return

            for other_student in students:

                if other_student != student and other_student[0] == number:
                    messagebox.showerror("Error", "This student number already exists.")
                    return

            try:

                mark1 = int(entries[2].get())
                mark2 = int(entries[3].get())
                mark3 = int(entries[4].get())
                exam = int(entries[5].get())

            except ValueError:

                messagebox.showerror("Error", "Please enter valid numbers for all marks.")
                return

            if not (0 <= mark1 <= 20 and 0 <= mark2 <= 20 and 0 <= mark3 <= 20):
                messagebox.showerror("Error", "Coursework marks must be between 0 and 20.")
                return

            if not (0 <= exam <= 100):
                messagebox.showerror("Error", "Exam mark must be between 0 and 100.")
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

        tk.Button(
            action_frame,
            text="Save Changes",
            bg=PURPLE,
            fg=WHITE,
            font=("Arial", 10, "bold"),
            command=save_update
        ).pack(anchor="w", pady=12)

    tk.Button(
        action_frame,
        text="Find Student",
        bg=PURPLE,
        fg=WHITE,
        font=("Arial", 10, "bold"),
        command=search_for_update
    ).pack(anchor="w", pady=12)


# ==========================================
# 16. MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("Student Manager")
root.geometry("1050x680")
root.config(bg=LIGHT)


# ==========================================
# 17. SIDEBAR
# ==========================================

sidebar = tk.Frame(
    root,
    bg=NAVY,
    width=230
)

sidebar.pack(side="left", fill="y")

sidebar.pack_propagate(False)


# SIDEBAR TITLE

tk.Label(
    sidebar,
    text="STUDENT\nMANAGER",
    bg=NAVY,
    fg=WHITE,
    font=("Arial", 19, "bold"),
    justify="left"
).pack(anchor="w", padx=20, pady=(25, 20))


# SIDEBAR BUTTON FUNCTION

def create_button(text, command):

    button = tk.Button(
        sidebar,
        text=text,
        bg=NAVY,
        fg="#D6D9E2",
        activebackground=PURPLE,
        activeforeground=WHITE,
        font=("Arial", 10),
        anchor="w",
        relief="flat",
        bd=0,
        padx=20,
        pady=9,
        command=command,
        cursor="hand2"
    )

    button.pack(fill="x", padx=10, pady=2)

    # Change colour when mouse enters

    button.bind(
        "<Enter>",
        lambda event: button.config(bg=SIDEBAR, fg=WHITE)
    )

    # Return to original colour when mouse leaves

    button.bind(
        "<Leave>",
        lambda event: button.config(bg=NAVY, fg="#D6D9E2")
    )


# MAIN MENU

create_button("⌂   Home", home)
create_button("▤   All Students", view_all)
create_button("⌕   Find Student", view_individual)
create_button("★   Highest Mark", highest_student)
create_button("↓   Lowest Mark", lowest_student)


# SEPARATOR

tk.Frame(
    sidebar,
    bg="#46536A",
    height=1
).pack(fill="x", padx=20, pady=12)


# EXTENSION OPTIONS

tk.Label(
    sidebar,
    text="MANAGE RECORDS",
    bg=NAVY,
    fg="#929DB0",
    font=("Arial", 8, "bold")
).pack(anchor="w", padx=20, pady=(0, 5))


create_button("⇅   Sort Records", sort_students)
create_button("+   Add Student", add_student)
create_button("✕   Delete Student", delete_student)
create_button("✎   Update Student", update_student)



# ==========================================
# 18. MAIN CONTENT AREA
# ==========================================

content = tk.Frame(
    root,
    bg=LIGHT
)

content.pack(side="right", fill="both", expand=True, padx=25, pady=20)


# ==========================================
# 19. PAGE HEADINGS
# ==========================================

heading = tk.Label(
    content,
    text="Student Manager",
    bg=LIGHT,
    fg=NAVY,
    font=("Arial", 22, "bold")
)

heading.pack(anchor="w")

subheading = tk.Label(
    content,
    text="Welcome to the Student Management System",
    bg=LIGHT,
    fg=GREY,
    font=("Arial", 10)
)

subheading.pack(anchor="w", pady=(5, 15))


# ==========================================
# 20. ACTION FRAME
# ==========================================

action_frame = tk.Frame(
    content,
    bg=LIGHT
)

action_frame.pack(fill="x", pady=5)


# ==========================================
# 21. SEARCH BOX
# ==========================================

search_frame = tk.Frame(
    content,
    bg=WHITE,
    padx=12,
    pady=12
)

search_frame.pack(fill="x", pady=10)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 11),
    width=35,
    bd=1,
    relief="solid"
)

search_entry.pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Search",
    bg=PURPLE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=15,
    command=search_student
).pack(side="left", padx=5)


# ==========================================
# 22. OUTPUT AREA
# ==========================================

result_frame = tk.Frame(
    content,
    bg=WHITE,
    padx=15,
    pady=15,
    highlightbackground="#DDD9EA",
    highlightthickness=1
)

result_frame.pack(fill="both", expand=True)

output = tk.Text(
    result_frame,
    bg=WHITE,
    fg=NAVY,
    font=("Consolas", 10),
    wrap="word",
    bd=0,
    padx=10,
    pady=10
)

output.pack(fill="both", expand=True)


# ==========================================
# 23. START PROGRAM
# ==========================================

home()

root.mainloop()