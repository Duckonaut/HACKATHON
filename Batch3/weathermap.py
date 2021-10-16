import requests
import json

API_KEY = '746e9c61af92a0707383733b40c34bde'

def main():
    location = (input('Latitude: '), input('Longitude: '))

    current_weather = json.loads(requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&appid={API_KEY}&lang=PL').text)

    if current_weather['sys']['country'] != 'PL':
        print('Not in Poland!')
        return

    print(current_weather['weather'][0]['description'])
    print(str(float(current_weather['main']['temp']) - 273.15))

if __name__ == '__main__':
    main()