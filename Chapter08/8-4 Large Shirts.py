def make_shirt(shirt_size='large', message='I Love Python'):
    print("\nThe shirt will be size " + shirt_size.title() +
          " with the following message:\n" + message)


# Make default shirt
make_shirt()

# Make medium shirt without message
make_shirt(shirt_size='medium')

# Any size shirt with any message
make_shirt('small', 'Hey')