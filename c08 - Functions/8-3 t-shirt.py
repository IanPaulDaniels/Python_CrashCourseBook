def make_shirt(shirt_size, message):
    print("\nThe shirt will be size " + shirt_size.title() +
          " with the following message:\n" + message)


# Call the function using positional arguments
make_shirt('large', 'ohyeah!')

# Call the function using keyword arguments
make_shirt(message='yas boi', shirt_size='medium')
