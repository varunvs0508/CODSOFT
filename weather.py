import requests

def get_weather_data(location):
    api_key = "e0f6d4ea647c90c1ee4f506c51052f90"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather_data = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
        return weather_data
    else:
        return None

def display_weather_data(weather_data, location):
    if weather_data:
        print(f"Weather in {location}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        print(f"Description: {weather_data['description']}")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    location = input("Enter city name or zip code: ")
    weather_data = get_weather_data(location)
    display_weather_data(weather_data, location)
