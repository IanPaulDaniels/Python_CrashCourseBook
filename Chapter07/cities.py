prompt = "Input cities you've visited before: (Enter 'quit' to exit) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to visit " + city.title())
