def hello():
    return "How can I help you?"

def add_contact(username, phone, contacts):
    contacts[username] = phone
    return "Contact added."

def change_contact(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(username, contacts):
    if username in contacts:
        return f"{username}'s phone number is: {contacts[username]}"
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts available."
    else:
        result = "All contacts:\n"
        for username, phone in contacts.items():
            result += f"{username}: {phone}\n"
        return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add":
            if len(args) == 2:
                username, phone = args
                print(add_contact(username, phone, contacts))
            else:
                print("Invalid command. Usage: add username phone")
        elif command == "change":
            if len(args) == 2:
                username, phone = args
                print(change_contact(username, phone, contacts))
            else:
                print("Invalid command. Usage: change username phone")
        elif command == "phone":
            if len(args) == 1:
                username = args[0]
                print(show_phone(username, contacts))
            else:
                print("Invalid command. Usage: phone username")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
