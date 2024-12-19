import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if any(contact['name'] == name for contact in contacts):
        print("Contact with this name already exists.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact {name} added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        choice = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= choice < len(contacts):
            print("Leave blank if no change is required.")
            name = input(f"New name ({contacts[choice]['name']}): ").strip() or contacts[choice]['name']
            phone = input(f"New phone ({contacts[choice]['phone']}): ").strip() or contacts[choice]['phone']
            email = input(f"New email ({contacts[choice]['email']}): ").strip() or contacts[choice]['email']

            contacts[choice] = {"name": name, "phone": phone, "email": email}
            print("Contact updated successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")


def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        choice = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= choice < len(contacts):
            removed_contact = contacts.pop(choice)
            print(f"Contact {removed_contact['name']} deleted successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")


def main():
    print("Welcome to Contact Management System!")
    contacts = load_contacts()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
