import csv

def load_contacts(file_name):
    contacts = {}
    with open (file_name, mode ="r" , newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            first_name              = row[0]
            last_name               = row[1]
            phone_number            = row[2]
            email                   = row[3]
            contacts[last_name]     = [first_name, phone_number, email]
    return contacts

def display_contact_info(contact_info):
    if contact_info:
        print("\nContact information:")
        print(f"First Name :    {contact_info[0]}")
        print(f"Phone Number :  {contact_info[1]}")
        print(f"Email :         {contact_info[2]}")
    else:
        print("No contact information found")


def main ():
    file_name = "clients.csv"
    contacts = load_contacts(file_name)
    last_name = input("Please insert a last name:").strip()
    contact_info = contacts.get(last_name)
    display_contact_info(contact_info)


main()