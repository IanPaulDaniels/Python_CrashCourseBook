def make_car(manufacturer, model_name, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    for key, value in car_info.items():
        car[key] = value

    return car


new_car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(new_car)
