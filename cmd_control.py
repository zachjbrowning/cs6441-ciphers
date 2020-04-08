from cipher_api import encode, decode, methods, overview, method_classes, in_depth
from db_control import load_data, save_data, reset_data

def prompt():
    print(' > ', end='')
    return input()

def help_cmd():
    print("Potential commands:")
    commands = ['?', 'q', 'n',  'e', 'd', 's', 'c', 'i', 'r']

    documentation = ['Help', 'Quit', 'Name change', 'Encode', 'Decode', 'Send message', 'Check messages', 'Information', 'Reset database']
    for i in range(len(commands)):
        print(' - [' + commands[i] + '] : ' + documentation[i])

    
def encode_decode(is_encode, msg=None):
    print("Please choose a method:")
    for i in range(len(methods)):
        print(' - ' + str(i) + ' : ' + methods[i])
    choice = prompt()
    correct = False
    while not correct:
        try:
            choice = int(choice)
            if choice < 0 or choice >= len(methods):
                raise ValueError
            correct = True
        except ValueError:
            correct = False
            print("Input was not an int or not a valid choice. Please choose a valid method. (Int between 0 and " + str(len(methods) - 1) + ")")
            choice = prompt()
    print("You are using the " + methods[choice] + " method!!")
    key = input("Please input your key: ")
    #NEED TO DO BETTER ERROR CHECKING HERE
    if choice in [2, 3]:
        key = "".join(key.split())
        while not valid_string(key):
            key = input("Invalid key. Please input a string of only alphabetic characters and spaces: ")
            key = "".join(key.split())
    elif choice is 4:
        key = " ".join(key.split())
        while not valid_string(key):
            key = input("Invalid key. Please input a string of only alphabetic characters and spaces: ")
            key = " ".join(key.split())
    else:
        if not key.isdigit():
            while not key.isdigit():
                key = input("Invalid key. Please input a number: ")
    if not msg:
        msg = input("Please input your message: ")
    if is_encode:
        return encode(method_classes[choice], key, msg)
    else:
        try: 
            result = decode(method_classes[choice], key, msg)
        except ValueError:
            return "Message is not decodable. It is either invalid or has been corrupted."
        return result

def valid_string(key_list):
    for word in key_list:
        for letter in word:
            if not letter.isalpha() and letter != ' ':
                return False 
    return True

def send_msg(name):
    data = load_data()

    recipient = input("Please input the name of the person you wish to contact: ")
    while recipient is '':
        recipient = input("Cannot have an empty name. Please try again: ")

    msg = encode_decode(True)
    if recipient in data['users']:
        data['users'][recipient][name] = msg 
    else:
        data['users'][recipient] = { name : msg, }

    save_data(data)

def check_msg(name):
    data = load_data()
    sender = None
    if name not in data['users']:
        print("No messages for you.")
        return
    else:
        if len(data['users'][name]) == 1:
            for person in data['users'][name]:
                sender = person 
            print("You have one message from "  + sender + ':')
            print("'" + data['users'][name][sender] + "'")
        else:
            persons = [x for x in data['users'][name]]
            print("You have multiple messages. Please select who's message you would like to read:")
            for i in range(len(persons)):
                print(" " + str(i) + ": " + persons[i])
            p_id = input("Please select a message: [0-" + str(len(persons) - 1) + "]: ")
            while not p_id.isdigit() or int(p_id) < 0 or int(p_id) > len(persons) - 1:
                p_id = input("Invalid choice. Please insert number between 0 and " + str(len(persons) - 1) + ": ")
            sender = persons[int(p_id)]
            print(sender, data['users'][name])
            print("The message from " + sender + " is:")
            print("'" + data['users'][name][sender] + "'")
    
    
    choice = input("Would you like to decode your message? [Y/N] ")

    while choice not in ['Y', 'y', 'N', 'n']:
        choice = input("Invalid choice. Please choose between yes ('Y') and no ('N'): ")

    if choice is 'Y' or choice is 'y':
        result = encode_decode(False, msg=data['users'][name][sender])
        print("Result:") 
        print(result)
    

def serve_info():
    print("Please choose which cipher you would like more info on:")
    for i in range(len(methods)):
        print(' - ' + str(i) + ' : ' + methods[i])
    choice = prompt()
    correct = False
    while not correct:
        try:
            choice = int(choice)
            if choice < 0 or choice >= len(methods):
                raise ValueError
            correct = True
        except ValueError:
            correct = False
            print("Input was not an int or not a valid choice. Please choose a valid method. (Int between 0 and " + str(len(methods) - 1) + ")")
            choice = prompt()
    print("A brief overview on the " + methods[choice] + " method:")
    print(overview[choice])
    print(' ')
    more = input("Would you like a more in depth explanation of how this cipher works? [Y/N] ")
    while more not in ['Y', 'y', 'N', 'n']:
        more = input("Invalid choice. Please choose between yes ('Y') and no ('N'): ")
    if more in ['Y', 'y']:
        print(in_depth[choice])
        print(' ')

    

def do_cmd(cmd, name):
    if cmd is '?':
        return help_cmd()
    elif cmd is 'e':
        print('\n', encode_decode(True), '\n')
    elif cmd is 'd':
        print('\n', encode_decode(False), '\n')
    elif cmd is 'i':
        serve_info()
    elif cmd is 'n':
        name = input("Please input your name: ")
        while name is '':
            name = input("Cannot have an empty name. Please try again: ")
    elif cmd is 'r':
        choice = input("Are you sure you want to reset the database? [Y/N] ")
        if choice is 'Y' or choice is 'y':
            print("Resetting databse.")
            data = reset_data()
            save_data(data)
        else:
            print("Database not reset")
    elif cmd is 's':
        send_msg(name)
    elif cmd is 'c':
        check_msg(name)
    elif cmd is '':
        pass
    else:
        print("Invalid command. For help with commands use '?")
    return name