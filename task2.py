def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact added. {name}: {phone}"


def change_contact(args, contacts):
    name, new_phone_number = args
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    name = args[0].lower()
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    if len(contacts) >= 1:
        return "\n".join(
            [f"{name}: {phone_number}" for name, phone_number in contacts.items()]
        )
    else:
        return "No contacts found."


def validate_command(args, expected_args_count, command_name):
    if len(args) != expected_args_count:
        print(
            f"Invalid command. Format: {command_name} [name] {'[phone]' if expected_args_count == 2 else ''}"
        )
        return False
    return True


def main():
    contacts = {'Admin': '1234567890'}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "bb"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi", "yo"]:
            print("How can I help you?")
        elif command == "add":
            if validate_command(args, 2, "add"):
                print(add_contact(args, contacts))
        elif command == "change":
            if validate_command(args, 2, "change"):
                print(change_contact(args, contacts))
        elif command == "phone":
            if validate_command(args, 1, "phone"):
                print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
