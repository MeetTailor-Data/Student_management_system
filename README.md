# Student Management System (Python)

A **menu-driven Student Management System** developed using core Python concepts.
This terminal-based application allows users to **add, view, update, and delete student records** efficiently. It is ideal for beginners practicing Python fundamentals.

---

## Project Description

This project manages student records using a Python **list of dictionaries**.
Each student record contains:

* Roll Number
* Student Name
* Marks

The program runs continuously until the user chooses to exit.

---

## Features

* Menu-driven interface
* Add new student records
* View all students
* Update student marks using roll number
* Delete student records
* Continuous execution using a loop
* Simple and readable logic

---

## Concepts Used

### Data Types

* List
* Dictionary
* Strings
* Integers
* Floating point numbers
* Booleans

### Control Statements

* `if / elif / else`
* `for` loop
* `while` loop

### Programming Concepts

* Functions
* List of dictionaries
* Input and output handling
* Basic search and update logic

---

## Project Structure

```
student-management/
│
├── StudentManagement.py   # Main program file
└── README.md              # Project documentation
```

---

## How to Run the Program

### Requirements

* Python 3.x installed on your system

### Steps

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the program using:

```bash
python StudentManagement.py
```

---

## Application Menu

```
====== Student Management System ======
1. Add Student
2. View Students
3. Update Marks
4. Delete Student
5. Exit
```

---

## Sample Output

```
Enter your choice (1-5): 1
Enter Roll No: 1
Enter New Student Name: Meet
Enter Students Marks: 88.5
Student Added Successfully
```

```
Enter your choice (1-5): 2
Roll No:  1
Name:  Meet
Marks:  88.5
```

---

## Edge Cases Handled

* No students available to display
* Student not found during update or delete
* Invalid menu choices
* Program runs until exit option is selected

---

## Future Improvements

* Prevent duplicate roll numbers
* Store student data in a file (CSV / JSON)
* Add grade calculation
* Search student by name

---

## Author

**Meet Tailor**
Python Programming Learner
GitHub: [https://github.com/MeetTailor-Data](https://github.com/MeetTailor-Data)

---

## License

This project is created for learning and educational purposes.

---

## Status

* Project Status: Completed
* Last Updated: 2026
