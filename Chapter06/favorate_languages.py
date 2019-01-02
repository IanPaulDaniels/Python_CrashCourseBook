favorate_languages = {
    # Name: Language
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in sorted(favorate_languages.keys()):
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorate_languages[name].title() + "!")

# for name, language in favorate_languages.items():
#     print(name.title() + "'s favorate language is " +
#           language.title() +
#           ".")
