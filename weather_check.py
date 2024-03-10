import requests

def get_weather(city):

    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q' : city,
        'appid' : '77d917c624d2b751c89314059cb71862',

        # this unit is used to get temperature result as Celsius.
        'units' : 'metric',
    }
    

    # the process before completed this code is, the live_date was printed for a time and were used to check the dictionary, key and value, to return the correct data that we need
    # it's the same as reading the JSON api respone example in the website
    live_data = requests.get(endpoint, params=params).json()

    # the cod != 404 is to check if the name of city is correct or not
    # A test was done by printing the result from asserting invalid city, the api return cod == 404
    if live_data['cod'] != '404':
        # base on api result, the weather in the dictionary contain a list, so that we need to clarify that list index which is 0 since it has only one list
        # if not then it will cause an error, so after we check the value of the key main inside that list, the value of main is the weather condition
        live_weather = live_data['weather'][0]['main']

        # so, to get the value of temperature we need to access to the key temp since it store the value of temperature
        # and to access to the key temp, we first need to access to this sub-dictionary which is main
        live_temperature = live_data['main']['temp']

        # We want to create a better UI which will return icon base on weather condition
        # So, we take the icon data as well to return and print out the icon.
        icon = live_data['weather'][0]['icon']

        # all the information we got, we return it as a dictionary
        return {
        'name': live_data['name'],
        'weather': live_weather,
        'temp': live_temperature,
        'icon': icon,
    }

    else:
        return 'city not found'