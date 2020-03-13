from cipher_api import encode, decode, methods, documentation, method_classes

def prompt():
    print(' > ', end='')
    return input()

def help_cmd():
    print("Potential commands:")
    commands = ['?', 'q', 'e', 'd', 'i']
    documentation = ['Help', 'Quit', 'Encode', 'Decode', 'Information']
    for i in range(len(commands)):
        print(' - [' + commands[i] + '] : ' + documentation[i])

    
def encode_decode(is_encode):
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

    msg = input("Please input your message: ")
    if is_encode:
        return encode(method_classes[choice], key, msg)
    else:
        return decode(method_classes[choice], key, msg)


def do_cmd(cmd):
    if cmd is '?':
        return help_cmd()
    elif cmd is 'e':
        print('\n', encode_decode(True), '\n')
    elif cmd is 'd':
        print("Result:")
        print('\n', encode_decode(False), '\n')
    elif cmd is 'i':
        print("For more info please email z5215283@ad.unsw.edu.au")
    else:
        print("Invalid command. For help with commands use '?")