import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Use metric for Celsius, or "imperial" for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print("\nWeather Information for", city)
            print("Temperature:", data["main"]["temp"], "°C")
            print("Weather:", data["weather"][0]["description"])
            print("Humidity:", data["main"]["humidity"], "%")
            print("Wind Speed:", data["wind"]["speed"], "m/s")
        else:
            print("Error:", data["message"])

    except requests.ConnectionError:
        print("Failed to connect to the API. Please check your internet connection.")

def main():
    api_key = 'a6584d20d248bd585b91e6c864e6e917' 
    city = input("Enter the city name: ")
    
    get_weather(api_key, city)

if __name__ == "__main__":
    main()
