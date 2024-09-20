import requests

def get_weather(city_name, api_key):
    # Base URL for the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city_name,      # City name
        'appid': api_key,    # Your API key
        'units': 'metric'    # Units of measurement: 'metric' for Celsius
    }
    
    # Make a GET request to the API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the JSON data
        
        # Extract relevant information from the JSON response
        city = data['name']
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Print weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_description.title()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        
    else:
        print("City not found or invalid API key. Please check your input.")

if __name__ == "__main__":
    # Get user input for the city name
    city_name = input("Enter the city name: ")
    
    # Replace with your own API key
    api_key = "YOUR_API_KEY_HERE"
    
    # Get weather data for the input city
    get_weather(city_name, api_key)
