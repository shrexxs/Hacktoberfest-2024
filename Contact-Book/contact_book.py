import json
import os

CONTACT_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to display all contacts
def display_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("\nNo contacts found.")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!")

# Function to search for a contact
def search_contact(contacts):
    query = input("Enter name to search: ").lower()
    found_contacts = [contact for contact in contacts if query in contact['name'].lower()]

    if found_contacts:
        print("\nSearch Results:")
        for idx, contact in enumerate(found_contacts):
            print(f"{idx + 1}. {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("\nNo matching contacts found.")

# Function to edit a contact
def edit_contact(contacts):
    display_contacts(contacts)
    try:
        index = int(input("Enter the contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]['name'] = input("Enter new name: ")
            contacts[index]['phone'] = input("Enter new phone number: ")
            contacts[index]['email'] = input("Enter new email address: ")
            print("\nContact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to delete a contact
def delete_contact(contacts):
    display_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"\nContact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to show menu
def show_menu():
    print("\nContact Book Menu:")
    print("1. View Contacts")
    print("2. Add New Contact")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contacts = load_contacts()
    while True:
        show_menu()
        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '6':
            print("\nExiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
