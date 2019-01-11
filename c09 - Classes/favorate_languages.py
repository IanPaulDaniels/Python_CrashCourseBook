from collections import OrderedDict

favorate_languages = OrderedDict()

favorate_languages['jen'] = 'python'
favorate_languages['sarah'] = 'c'
favorate_languages['edward'] = 'ruby'
favorate_languages['phil'] = 'python'

for name, language in favorate_languages.items():
    print(name.title() + "'s favorate language is " +
        language.title() + ".")