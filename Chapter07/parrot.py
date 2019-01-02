prompt = "I will repeat everything you say!\n Enter 'quit' to exit the program: "

active = True

while active:
    message = input(prompt)
    if message != 'quit':
        print(message + "\n")
    else:
        active = False
