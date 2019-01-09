from collections import OrderedDict

glossary = OrderedDict()

glossary['list'] = 'Array to store values'
glossary['dictionary'] = 'store key/value pairs'
glossary['if else'] = 'desicion making structure'

for key, value in glossary.items():
    print(key.title() + ': ' + value.title())
