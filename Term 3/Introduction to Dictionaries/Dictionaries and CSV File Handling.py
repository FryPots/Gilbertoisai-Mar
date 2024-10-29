import csv

def load_contacts(filename):
    contacts = {}
    with open(filename, mode= "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            first_name = row[0]
            last_name  = row[1]
            phone_num  = row[2]
            email      = row[3]
            contacts[last_name] = [first_name, phone_num, email]
    return contacts

def display_contact_info(contact_info):
    if contact_info:
        print("\nContact Info: ")
        print(f"first_name:   {contact_info[0]}")
        print(f"phone number: {contact_info[1]}")
        print(f"email:        {contact_info[2]}")
    else:
        print(f"Error Match for {contact_info} not Found")

def main():
    filename = "clients.csv"
    
    contacts = load_contacts(filename)
    
    last_name = input("please enter a last name to look up: ").strip()
    contact_info = contacts.get(last_name)
    display_contact_info(contact_info)
    
main()