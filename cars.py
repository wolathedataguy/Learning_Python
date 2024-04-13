def car_info(manufacturer, model_name, **car_details):
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    for key, value in car_details.items():
        car[key] = value
    print(car)

car_info('Acura','RDX', color ='purple', manufacture_date = 2009)
car_info('Subaru', 'Outback', color ='blue', tow_package = True)