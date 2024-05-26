import time
from fetchWeather import fetch_weather


def mainMenu():
    print("Hey There!! What would like to do today?")
    userResponse = input("1. Get Weather details\n2. Nothing. Just Hanging!!\n>>> ")
    weather_keywords = ['weather','forecast','temperature']
    if (userResponse == "1" or any(keyword in userResponse.lower() for keyword in weather_keywords)):
        print("Sure let me summon the weather god!!")
        time.sleep(1.5)
        checkWeather = input("1. Fetch Weather for 1 location\n2. Fetch Weather for multiple Location\n>>> ")
        if(checkWeather == "1"):
            location = input("Please enter your current city >> ")
            fetch_weather(location)
        elif(checkWeather == "2"):
            locations = input("Enter the names of the city Separated by comma >> ").split(',')
            for location in locations:
                fetch_weather(location)
        else:
            print("Seems like you have entered a wrong input.")
            mainMenu()
        
    else:
        print("Seems like you have entered a wrong input. Please try again.\nTry something like Give me weather report! (or) just type 1\n\n")
        time.sleep(1)
        mainMenu()



mainMenu()