from cmd_control import do_cmd, prompt


def startup():
    print("Welcome to my encoding/decoding tool!")
    return input("Please input your name: ")

def shutdown():
    print("Thankyou for using my encoding/decoding tool. See you next time!")

def interface():
    
    name = startup() 
    while name is '':
        name = input("Cannot have an empty name. Please try again: ")
    
    print("Please input a command. For help on commands, use '?'")
    cmd = prompt()
    
    while cmd is not 'q':
        name = do_cmd(cmd, name)
        print("Please input a command. For help on commands, use '?'")
        cmd = prompt()

    shutdown() 


if __name__ == "__main__":
    interface()

