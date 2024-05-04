def input_error(func):
    '''The decorator to process erros in user input'''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me the name"
        except KeyError:
            return "Ask about one of your contact, or use 'all' command"

    return inner

def parse_input(user_input):
    '''The function to parse user input'''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    '''Process command "add" with str arguments "name" and "Phone number"'''
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    '''Process command "change" with str arguments "name" and "Phone number"'''
    name, phone = args
    contacts[name] = phone
    return "Contact changed"

@input_error
def return_phone(args, contacts):
    '''Process command "phone" with str argument "name"'''
    username = args[0]
    return contacts[username]

def main():
    '''Main function to control the bot'''
    contacts = {}
    contacts = {"Yevhen": "0685279337", "Nataliia": "0986421987", "Pavlo": "0952334876"} # Uncomment for testing
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(return_phone(args, contacts))
        elif command == "all":
            try:
                max_key_length = max(len(str(key)) for key in contacts)
                for key, value in contacts.items():
                    print(f"{str(key):<{max_key_length}} : {value}")
            except ValueError:
                print("No contacts found")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
