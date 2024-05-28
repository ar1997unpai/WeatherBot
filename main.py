import time
from fetchWeather import fetch_weather, fetch_weather_nextday
import spacy


# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")


# function to extract location and keyword (today, tomorrow)
def extract_locations_and_keywords(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    keywords = [ent.text for ent in doc.ents if ent.label_ == "DATE"]# Extracting dates or other relevant keywords
    #print(f">>>>>>>>>>>>>>>>>locations :{locations}\nkeywords : {keywords}")
    return locations, keywords


#function to bypass all the menu flows and directly get weather details
def quick_weather_check(text):
    """Function to handle quick weather queries."""
    locations, keywords = extract_locations_and_keywords(text)
    if locations:
        for location in locations:
            fetch_weather(location.strip())  # Calling the fetchWeather function
    else:
        print("Couldn't detect any location. Please try again.")





def mainMenu():
    print("Hey There!! What would like to do today?")
    userResponse = input("1. Get Weather details\n2. Nothing. Just Hanging!!\n>>> ")
    weather_keywords = ['weather','forecast','temperature','climate','cold','hot','rain','raining','forcast'] #Comparison list
    locations, keywords = extract_locations_and_keywords(userResponse)
    if (userResponse == "1"): # checks for the user selected option or occurance of the word from the comparisonlist
        print("Sure let me summon the weather god!!")
        time.sleep(1.5)
        locations_input = input("Enter the name of the city (or multiple cities separated by commas) >> ")

        # extracting location using spacy package
        if not locations:
            locations = locations_input.split(',') #When no location is found, fallback to default flow splitting it to a list

        for location in locations:
            fetch_weather(location.strip()) # Calling the fetchWeather func - .strip() removes white spaces 
    
    elif any(keywords in userResponse.lower() for keywords in weather_keywords):
        if "tomorrow" in userResponse.lower() and locations:
            for location in locations:
                fetch_weather_nextday(location.strip())
        else:        
            quick_weather_check(userResponse)
        
    else:
        print("Seems like you have entered a wrong input. Please try again.\nTry something like Give me weather report! (or) just type 1\n\n")
        time.sleep(1)
        mainMenu()



mainMenu()