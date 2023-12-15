import json

class Phonebook:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.contacts = self.load_data()

    def load_data(self):
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        self.save_data()

    def view_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Phone: {self.contacts[name]}")
        else:
            print("Contact not found")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_data()
            print("Contact deleted")
        else:
            print("Contact not found")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact found - Name: {name}, Phone: {self.contacts[name]}")
        else:
            print("Contact not found")

    def modify_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            self.save_data()
            print("Contact modified")
        else:
            print("Contact not found")


phonebook = Phonebook('phonebook_storage.json')

while True:
    print("\n1. Add Contact\n2. View Contact\n3. Delete Contact\n4. Search Contact\n5. Modify Contact\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        phonebook.add_contact(name, phone)
    elif choice == '2':
        name = input("Enter contact name: ")
        phonebook.view_contact(name)
    elif choice == '3':
        name = input("Enter contact name: ")
        phonebook.delete_contact(name)
    elif choice == '4':
        name = input("Enter contact name: ")
        phonebook.search_contact(name)
    elif choice == '5':
        name = input("Enter contact name: ")
        new_phone = input("Enter new phone number: ")
        phonebook.modify_contact(name, new_phone)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")