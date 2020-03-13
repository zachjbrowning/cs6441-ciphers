from cmd_control import do_cmd, prompt

def startup():
    print("Welcome to my encoding/decoding tool!")
    print("Please input a command. For help on commands, use '?'")
    return prompt()

def shutdown():
    print("Thankyou for using my encoding/decoding tool. See you next time!")

def interface():
    cmd = startup() 

    while cmd is not 'q':
        do_cmd(cmd)
        print("Please input a command. For help on commands, use '?'")
        cmd = prompt()

    shutdown() 


if __name__ == "__main__":
    interface()

