import requests

API_KEY = '082e3b1a2b2a188abf3e1f06a77a0bc7'

def get_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    data = response.json()

    if data['cod'] == 200:

        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        feels_like_temperature = data['main']['feels_like']
        weather_condition = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f'🌦️  {city_name}, {country}')
        print(f'Temperature: {temperature}°C')
        print(f'Feels like: {feels_like_temperature}°C')
        print(f'Condition: {weather_condition}')
        print(f'Humidity: {humidity}%')

    else:
        print(f'Error: {data['message']}')


while True:
    city = input('\n> ENTER City (or quit): ')

    if city == 'quit':
        break
    else:
        get_weather(city)