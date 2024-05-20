from wsgiref import headers
import requests

def fetch_weather(loc):
    apiKey = "583f28380c46473c90a112459242005"
    print(f"checking weather in your city - {loc}!")
    url = f"http://api.weatherapi.com/v1/current.json?q={loc}"
    headers ={"key":apiKey}
    
    weatherResponseRaw = requests.get(url,headers)
    if weatherResponseRaw.status_code == 200:
        weatherResponse = weatherResponseRaw.json()
        
        print("Temp in Celcius - ",weatherResponse["current"]["temp_c"])
    