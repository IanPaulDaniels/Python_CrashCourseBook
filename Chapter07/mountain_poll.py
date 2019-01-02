responses = {}

polling_active = True

while polling_active:
    name = input("Enter your name: ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like another person to respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n---\tPoll Results\t---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

print(responses)
