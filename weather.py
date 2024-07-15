import os
import json
import requests
from dotenv import load_dotenv, dotenv_values

def can_be_int(inpt):
    try:
        int(inpt)
        return True
    except ValueError:
        return False

def get_valid_input():
    while True:
        usrinpt = input("How many days you want to see weather forecast for(1-10): ")
        if can_be_int(usrinpt):
            usrinpt = int(usrinpt)
            if 1 <= usrinpt <=10:
                return usrinpt
            else:
                print("You entered an unvalid input. Please enter a number from 1 to 10: ")
        else:
            print("You entered an unvalid input. Please enter a number from 1 to 10: ")
        

load_dotenv()

KEY = os.getenv("API_KEY")

request_url="http://api.weatherapi.com/v1"

print("Forecast(F)/Current(C)")
forc = input("")

if forc.upper() == "C":
    request_url += "/current.json?key="+KEY
    print("Enter a location to see the current temperature of it: ")
    loc = input("")
    request_url += "&q="+loc
    response = requests.get(request_url)
    if response.status_code == 200:
        weather_data = response.json()
        print("Current Temperature in " + weather_data["location"]["name"] + ", "+ weather_data["location"]["region"]+ ", "+ weather_data["location"]["country"]+ " is " + (str)(weather_data["current"]["temp_c"]) + ", " + weather_data["current"]["condition"]["text"]+".")
elif forc.upper() == "F":
    request_url +="/forecast.json?key="+KEY
    print("Enter a location to see the current temperature of it: ")
    loc = input("")
    request_url += "&q="+loc
    days = get_valid_input()
    request_url +="&days=" + str(days) +"&aqi=no&alerts=no"
    response = requests.get(request_url)
    if response.status_code== 200:
        weather_data = response.json()
        print(str(days) + " Days Forecast of " + weather_data["location"]["name"] + ":")
        for i in range(days):
            print("Max and Min temperature in " + weather_data["location"]["name"] + ", "+ weather_data["location"]["region"]+ ", "+ weather_data["location"]["country"]+ " in " + weather_data["forecast"]["forecastday"][i]["date"]+ " are " + str(weather_data["forecast"]["forecastday"][i]["day"]["maxtemp_c"]) + "/" + str(weather_data["forecast"]["forecastday"][i]["day"]["mintemp_c"]))
