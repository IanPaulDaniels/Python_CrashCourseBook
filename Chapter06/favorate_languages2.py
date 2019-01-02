favorate_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'c'],
    'phil': ['python', 'javascript'],
}

for name, languages in favorate_languages.items():
    print(name.title() + "'s favorate languages are: ")

    for language in languages:
        print("\t-" + language.title())
