import requests
import json


file = open('api-key.txt', 'r')

API_KEY = file.read()

file.close()

def toCelsius(temperature):
    return int(temperature - 273.15)

def printData(dailyInfo):
    print(f'\t\tTemperatures between {toCelsius(dailyInfo["temp"]["min"])} and {toCelsius(dailyInfo["temp"]["max"])} degrees Celsius')
    print(f'\t\tWeather is {dailyInfo["weather"][0]["description"]}')

def main():
    location = (input('Latitude: '), input('Longitude: '))

    locationQuery = json.loads(requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&appid={API_KEY}&lang=EN').text)
    if locationQuery['cod'] != 200:
        print(f'API Error {locationQuery["cod"]}')
        return

    forecast = json.loads(requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={location[0]}&lon={location[1]}&exclude=current,hourly,minutely,alerts&appid={API_KEY}&lang=EN').text)

    

    if len(locationQuery['name']) > 0:
        print(f"Weather for {locationQuery['name']}")
    else:
        directionLat = ''
        if int(location[0]) < 0:
            directionLat = 'W'
        else:
            directionLat = 'E'

        directionLon = ''
        if int(location[1]) < 0:
            directionLon = 'S'
        else:
            directionLon = 'N'

        print(f"Weather for {abs(int(location[0]))}{directionLat}, {abs(int(location[1]))}{directionLon}")

    
    print('\tToday:')
    printData(forecast['daily'][0])
    print('\tTomorrow:')
    printData(forecast['daily'][1])
    print('\tIn 2 days:')
    printData(forecast['daily'][2])
    print('\tIn 3 days:')
    printData(forecast['daily'][3])

    

if __name__ == '__main__':
    main()