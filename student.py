students=[]
def add_student():
  roll_no=int(input("Enter Roll No: "))
  name=input("Enter New Student Name: ")
  marks=float(input("Enter Students Marks: "))

  student = {
        "roll": roll_no,
        "name": name,
        "marks": marks
    }
  students.append(student)
  print("Student Added Successfully")
def show_student():
  if not students:
    print("No Students to Show")
    return
  for i in students:
    print("Roll No: ",i["roll"])
    print("Name: ",i["name"])
    print("Marks: ",i["marks"])

def update_student():
  roll_no=int(input("Enter Roll No: "))
  for s in students:
    if s["roll"]==roll_no:
      new_marks=float(input("Enter Students Marks that you would to Update: "))
      s["marks"]=new_marks
      print("Marks Updated Successfully")
      return
  print("Student Not Found")
def delete_student():
  roll_no=int(input("Enter Roll No: "))
  for s in students:
    if s["roll"]==roll_no:
      students.remove(s)
      print("Student Deleted Successfully")
      return
  print("Student Not Found")
while True:
    print("====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice=='1':
      add_student()
    elif choice=='2':
      show_student()
    elif choice=='3':
      update_student()
    elif choice=='4':
      delete_student()
    elif choice=='5':
      break
    else:
      print("Invalid Choice")