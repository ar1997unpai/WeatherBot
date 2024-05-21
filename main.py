import time
from fetchWeather import fetch_weather


def mainMenu():
    print("Hey There!! What would like to do today?")
    userResponse = str(input("1. Get Weather details\n2. Nothing. Just Hanging!!\n>>> "))
    if userResponse == "1":
        print("Sure let me summon the weather god!!")
        time.sleep(1.5)
        checkWeather = str(input("1. Fetch Weather for 1 location\n2. Fetch Weather for multiple Location\n>>> "))
        if(checkWeather == "1"):
            location = str(input("Please enter your current city >> "))
            fetch_weather(location)
        elif(checkWeather == "2"):
            locations = input("Enter the names of the city Separated by comma >> ").split(',')
            for location in locations:
                fetch_weather(location)
        else:
            print("Wrong entry. Please try again.")
            mainMenu()
        
    else:
        print("Sure Let me know if anything needed.")



mainMenu()