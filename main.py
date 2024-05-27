import time
from fetchWeather import fetch_weather


def mainMenu():
    print("Hey There!! What would like to do today?")
    userResponse = input("1. Get Weather details\n2. Nothing. Just Hanging!!\n>>> ")
    weather_keywords = ['weather','forecast','temperature'] #Comparison list
    if (userResponse == "1" or any(keyword in userResponse.lower() for keyword in weather_keywords)): # checks for the user selected option or occurance of the word from the comparisonlist
        print("Sure let me summon the weather god!!")
        time.sleep(1.5)
        locations_input = input("Enter the name of the city (or multiple cities separated by commas) >> ")
        locations = locations_input.split(',') # when multiple cities are given, splitting it to a list

        for location in locations:
            fetch_weather(location.strip()) # Calling the fetchWeather func - .strip() removes white spaces 
        
    else:
        print("Seems like you have entered a wrong input. Please try again.\nTry something like Give me weather report! (or) just type 1\n\n")
        time.sleep(1)
        mainMenu()



mainMenu()