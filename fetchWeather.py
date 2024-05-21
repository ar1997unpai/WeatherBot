from wsgiref import headers
import requests
import time

def fetch_weather(loc):
    apiKey = "583f28380c46473c90a112459242005"
    url = f"http://api.weatherapi.com/v1/current.json?q={loc}"
    headers ={"key":apiKey}
    
    try:
        weatherResponseRaw = requests.get(url,headers)
        if weatherResponseRaw.status_code == 200:
            weatherResponse = weatherResponseRaw.json()
            print("\n")
            print(f"checking weather in your city - {loc}!")
            time.sleep(1)
            print("\n")
            print(f"Weather Report for {weatherResponse["location"]["name"]} as of {weatherResponse["location"]["localtime"]}")
            print(f"Temperature - {weatherResponse["current"]["temp_c"]} C")
            print(f"Feels like - {weatherResponse["current"]["feelslike_c"]} C")
            print(f"Humidity - {weatherResponse["current"]["humidity"]}")
            print(f"Weather Condition - {weatherResponse["current"]["condition"]["text"]}")
            print(f"UV index - {weatherResponse["current"]["uv"]}")
        else:
            print("Unable to fetch weather details. Please try again later")
    except requests.RequestException as e:
        print("Error in ",e)

        
        
        
    