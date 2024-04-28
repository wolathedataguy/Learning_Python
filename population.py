def city_country(city, country, population =''):
    """Returns the a string stating the city and country"""
    if population:
        message = f'{city}, {country} - population {population}'
    else:
        message = f'{city}, {country}'
    return message
