# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
    
def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    f = open("list_save.txt","r")
    #TODO HINT: Print each student in the 'students' list
    print(f"_____________________________________") 

# Add a new student to the list
def add_student():
    #TODO HINT: Ask the user for the student's name.
    #TODO Append the student's name to the 'students' list
    #TODO display the updated list
    pass #! After complete the function remove 'pass'

# Remove a student from the list by name
def remove_student():
    #TODO HINT: Ask the user for the student's name to remove
    #TODO Check if the student is in the list, then remove it
    #TODO If the student is not found, print an error message
    #TODO display the updated list
    pass #! After complete the function remove 'pass'

# remove a student from the end of the list
def pop_student():
    #TODO HINT: Remove the last student from the list
    #TODO If the list is not empty, display the name of the student removed
    #TODO If the list is empty, print a message saying there are no students left
    #TODO display the updated list
    pass #! After complete the function remove 'pass'

# Update a student's name in the list
def update_student():
    #TODO HINT: ask for the current name of the student
    #TODO Check if the student is in the list, then ask for the new name
    #TODO Update the student's name in the list
    #TODO If the student is not found, print an error message
    #TODO display the updated list
    pass #! After complete the function remove 'pass'

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            pop_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            break
        #TODO depending of the user choice option (1 - 5), call the correct function

# Start the program

f = open("list_save.txt","a")
f.close()
f = open("list_save.txt","r")
print(f.read())
menu()