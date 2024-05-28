from wsgiref import headers
import requests
import time
from datetime import datetime
from functools import lru_cache


currentTime = datetime.now() # function to get current time


@lru_cache(maxsize=100) # decorator for the caching stores max of 100 results
def fetch_weather(loc):
    apiKey = "583f28380c46473c90a112459242005" #api key
    url = f"http://api.weatherapi.com/v1/forecast.json?q={loc}"
    headers ={"key":apiKey}
    
    try:
        weatherResponseRaw = requests.get(url,headers)
        if weatherResponseRaw.status_code == 200: #When city name exists, the API fetches the details
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
            print(f"UV index - {weatherResponse["current"]["uv"]}\n\n")
            
            with open("WeatherReport.txt","w") as file: #writing the weather details to a external file
                file.write ("\n\n **************************************************************************************\n")
                file.write(f"Weather Report for {weatherResponse['location']['name']} as of {weatherResponse['location']['localtime']}\n")
                file.write(f"Temperature - {weatherResponse['current']['temp_c']} C\n")
                file.write(f"Feels like - {weatherResponse['current']['feelslike_c']} C\n")
                file.write(f"Humidity - {weatherResponse['current']['humidity']}\n")
                file.write(f"Weather Condition - {weatherResponse['current']['condition']['text']}\n")
                file.write(f"UV index - {weatherResponse['current']['uv']}")


        else:
            print("Unable to fetch weather details. Please try again later")
            errorWeatherResponse = weatherResponseRaw.json()
            with open("logs.txt","a") as file: #logging all the errors into logs.txt
                file.write("\n\n ************* \n")
                file.write(f"Error Log of {currentTime} >>>> \n")
                file.write(f"Error Status code : {weatherResponseRaw.status_code}\n")
                file.write(f"Error code : {errorWeatherResponse["error"]["code"]} \t - \t Error Message : {errorWeatherResponse["error"]["message"]} - {loc}")                
    except requests.RequestException as e:
        with open("logs.txt","a+") as file:
            file.write("\n\n ************* \n")
            file.write(f"Error Log of {currentTime} >>>> \n")
            file.write(f"Error Status code : {e}")        
        
        
    