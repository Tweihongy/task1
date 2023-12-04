import requests


api_key = '3b4e56db1ce29aa30507e5ecd967a134'


city_name = input("Enter the city name: ")


url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'


response = requests.get(url)


if response.status_code == 200:

    weather_data = response.json()
    
    weather_description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"Weather in {city_name}: {weather_description}")
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

else:

    print("Error {}: {}".format(response.status_code, response.text))
