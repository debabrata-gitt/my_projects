import json
from pathlib import Path

DATABASE = "contacts.json"


def load_contacts():
    if Path(DATABASE).exists():
        with open(DATABASE, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(DATABASE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("\nContact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found!")
        return

    print("\n----- ALL CONTACTS -----")

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


def search_contact(contacts):
    name = input("Enter name to search: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact Found!")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return

    print("\nContact not found!")


def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("\nContact deleted successfully!")
            return

    print("\nContact not found!")


def update_contact(contacts):
    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            print("\nLeave blank if you don't want to change anything.")

            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            save_contacts(contacts)

            print("\nContact updated successfully!")
            return

    print("\nContact not found!")


contacts = load_contacts()

while True:

    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("\nInvalid choice! Please try again.")