contacts = {}
def print_menu():
    print(" MENU ")
    print("1. Add contact")
    print("2. Remove contact")
    print("3. View contact")
    print("4. Search contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = {"phone": phone,}
    print("Contact added.")

def remove_contact():
    name = input("Enter name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print("Contact removed.")
    else:
        print("Contact not found in the book.")

def view_contact():
    name = input("Enter name of the contact to view: ")
    if name in contacts:
        print("CONTACT DETAILS")
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found in the book.")

def search_contact():
    search_term = input("Enter search term: ")
    results = [key for key in contacts.keys() if search_term.lower() in key.lower()]
    if results:
        print("SEARCH RESULTS:")
        for name in results:
            print(name)
    else:
        print("No contacts found.")

while True:
    print_menu()
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        remove_contact()
    elif choice == "3":
        view_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")