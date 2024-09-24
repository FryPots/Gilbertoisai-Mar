
code = (r'''# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
def listify(text, c):
    out = ""
    return_list = []
    for i in (text):
        if i == c:
            return_list.append(out)
            out = ""
        else:
            out = out + i
    return return_list

def lined(text):
    a = ""
    for i in (text):
        if i == "\n":
            a = ""
        else:
            a = a + "_"
    print(f"""{a}
{text}          
{a}""")
    

def save():
    global file
    open(file, "w").write("\n".join(student_list))

def display_students():
    lined(f"Current students:\n{student_list}")
    #TODO HINT: Print each student in the 'students' list

# Add a new student to the list
def add_student(name):
    #TODO HINT: Ask the user for the student's name.
    print()
    student_list.append(name)
    #TODO Append the student's name to the 'students' list
    display_students()
    #TODO display the updated list
    #! After complete the function remove 'pass'

# Remove a student from the list by name
def remove_student(name):
    #TODO HINT: Ask the user for the student's name to remove
    #TODO Check if the student is in the list, then remove it
    for i in (student_list):
        if name == i:
            student_list.remove(name)
            display_students()
            return()
    #TODO If the student is not found, print an error message
    
    lined("Error, student name not found.")
    #TODO display the updated list
    #! After complete the function remove 'pass'

# remove a student from the end of the list
def pop_student():
    if len(student_list) != 0:
        student_list.pop()
        display_students()
    else:
        lined("Error, there are no students left.")
    #TODO HINT: Remove the last student from the list
    #TODO If the list is not empty, display the name of the student removed
    #TODO If the list is empty, print a message saying there are no students left
    #TODO display the updated list
    #! After complete the function remove 'pass'

# Update a student's name in the list
def update_student(name):
    #TODO HINT: ask for the current name of the student
    #TODO Check if the student is in the list, then ask for the new name
    for i in range(len(student_list)):
        if student_list[i] == name:
            newname = input("Type the new name:")
    #TODO Update the student's name in the list
            student_list[i] = newname
            display_students()
            return
    #TODO If the student is not found, print an error message
    lined("Error, student name not found.")


    #TODO display the updated list
    #! After complete the function remove 'pass'

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Save & Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student(input("Type the name of the student: "))
        elif choice == "2":
            remove_student(input("Type the name of the student: "))
        elif choice == "3":
            pop_student()
        elif choice == "4":
            update_student(input("Type the name of the student: "))
        elif choice == "5":
            save()
            break
        #TODO depending of the user choice option (1 - 5), call the correct function

# Start the program
file = "list_save.txt"
open(file, "a").close()
student_list = listify((open(file, "r").read()), "\n")
menu()''')

open("student_list_incomplete.py", "w").write(code)

open("list_save.txt", "w").write(r"""Peter
John
Simon
Andrew
Phillip
Judas
Matthew
Paul
Bartholomew
James the great
James the lesser
Jude
Thomas""")