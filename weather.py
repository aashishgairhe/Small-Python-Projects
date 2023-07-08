import requests
from dotenv import load_dotenv
import os

load_dotenv()
apiKey = os.environ['APIKEY']

weatherInput = input("enter the location: ")
weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={weatherInput}&units=imperial&APPID={apiKey}")

if weatherData.json()['cod'] == "404":
    print("location not found.")
else:
    weather = weatherData.json()['weather'][0]['main']
    temperature = weatherData.json()['main']['temp']
    description = weatherData.json()['weather'][0]['description']


    print(f"the weather of {weatherInput} is {weather}, {description} to be exact \nThe temperature of {weatherInput} is {temperature}")