def cityCountry(city, country, population=''):
    if population:
        formatted_text = city + ', ' + country + ' - Population ' + str(population)
    else: 
        formatted_text = city + ', ' + country
    return formatted_text.title()

# city = cityCountry('san juan', 'pr', 250001)

# print(city)