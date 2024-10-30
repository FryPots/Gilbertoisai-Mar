import csv

def load_contacts(file_name):
    contacts : dict = {}
    with open(file_name, mode ="r" , newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            first_name              = row[0]
            last_name               = row[1]
            phone_number            = row[2]
            email                   = row[3]
            full_name               = f"{first_name} {last_name}"
            contacts[last_name]     = [full_name, phone_number, email]
    return contacts

def display_contact_info(contact_info):
    if contact_info:
        print("\nContact information:")
        print(f"Name :          {contact_info[0]}")
        print(f"Phone Number :  {contact_info[1]}")
        print(f"Email :         {contact_info[2]}")
        print()
    else:
        print("No contact information found")


def main ():
    file_name : str  = "clients.csv"
    contacts  : dict = load_contacts(file_name)
#    print(contacts)
    last_name = (input("Please insert a last name:").strip()).capitalize()
    contact_info : list = contacts.get(last_name)
    display_contact_info(contact_info)
    main()

if __name__ == "__main__":
    main()