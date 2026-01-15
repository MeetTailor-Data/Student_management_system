# Student Management System (Python)

This is a **menu-driven Student Management System** built using core Python concepts.
The application allows users to **add, view, update, and delete student records** using a simple terminal-based interface.

---

## Project Description

The Student Management System helps manage basic student information such as:

* Roll Number
* Student Name
* Marks

The program runs continuously using a loop and allows the user to choose operations from a menu until they decide to exit.

This project is ideal for **beginners learning Python**, especially to understand how data is stored and manipulated using lists and dictionaries.

---

## Features

* Menu-driven interface
* Add new student records
* View all students
* Update student marks using roll number
* Delete student records
* Uses list of dictionaries for data storage
* Continuous execution until exit
* Simple and readable structure

---

## How the Program Works

1. The program displays a menu with options.
2. The user selects an option (1–5).
3. Based on the choice, a specific function is executed.
4. Student data is stored in memory using a list.
5. The program repeats until the user chooses Exit.

---

## Functions Used

### 1. add_student()

* Takes roll number, name, and marks as input
* Stores student data in a dictionary
* Appends the dictionary to the students list

### 2. show_student()

* Displays all student records
* Checks if the list is empty before displaying

### 3. update_student()

* Searches for a student using roll number
* Updates marks if the student exists

### 4. delete_student()

* Deletes a student record based on roll number

---

## Concepts Used

### Data Types

* int (Roll Number)
* float (Marks)
* string (Student Name)
* list (Stores all students)
* dictionary (Stores individual student details)

### Control Statements

* if / elif / else
* for loop
* while loop
* break

### Functions

* Function definition and calling
* Code reusability

---

## Sample Menu Output

```
====== Student Management System ======
1. Add Student
2. View Students
3. Update Marks
4. Delete Student
5. Exit
```

---

## Advantages of This Project

* Beginner-friendly
* Improves logical thinking
* Strengthens understanding of Python basics
* Useful for academic practicals
* Can be extended with file handling or database

---

## Possible Enhancements

* Store data permanently using files (CSV / TXT)
* Add search functionality
* Sort students by marks or roll number
* Add validation for duplicate roll numbers
* Convert to GUI or web-based application

---

## Conclusion

This Student Management System is a simple yet powerful Python project that demonstrates how real-world problems can be solved using basic programming concepts. It serves as a strong foundation for learning **data handling, control flow, and function-based programming** in Python.
