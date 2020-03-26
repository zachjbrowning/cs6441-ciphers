from cipher_api import encode, decode, methods, documentation, method_classes
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
    if choice in [2, 3, 4]:
        key = "".join(key.split())
    if not msg:
        msg = input("Please input your message: ")
    if is_encode:
        return encode(method_classes[choice], key, msg)
    else:
        return decode(method_classes[choice], key, msg)

def send_msg(name):
    data = load_data()

    recipient = input("Please input the name of the person you wish to contact: ")

    msg = encode_decode(True)
    
    data['users'][recipient] = msg

    save_data(data)

def check_msg(name):
    data = load_data()
    if name not in data['users']:
        print("No messages for you.")
        return
    else:
        print("You have a message:")
        print("'" + data['users'][name] + "'")
    
    choice = input("Would you like to decode your message? [Y/N] ")

    while choice not in ['Y', 'y', 'N', 'n']:
        choice = input("Invalid choice. Please choose between yes ('Y') and no ('N'): ")

    if choice is 'Y' or choice is 'y':
        result = encode_decode(False, msg=data['users'][name])
        print("Result:") 
        print(result)
    



def do_cmd(cmd, name):
    if cmd is '?':
        return help_cmd()
    elif cmd is 'e':
        print('\n', encode_decode(True), '\n')
    elif cmd is 'd':
        print("Result:")
        print('\n', encode_decode(False), '\n')
    elif cmd is 'i':
        print("For more info please email z5215283@ad.unsw.edu.au")
    elif cmd is 'n':
        name = input("Please input your name: ")
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
    else:
        print("Invalid command. For help with commands use '?")
    return name