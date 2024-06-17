import requests
import json
from datetime import datetime 

api_key = '' # write your key here

#SETTING UP API#
def get_weather(api_key, location): # defining function 'get_weather'

    # makes a GET request to the OpenWeatherMap API
    result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
    # if statement provides validation /if 404 error = "invalid loation"
    if result.json()['cod'] == '404':
        print("Invalid location!")
        # using return within function to make it reuseable
        return None
    # if user input valid and we get a 200 response, returns the JSON data of that location
    return result.json()

#GETTING INPUT#    
while True: 
    location = input("Hi please input a Location: ")
    location = location.capitalize()

    weather_data = get_weather(api_key, location)
    if weather_data: 
        break # if weather data valid = break loop and go to next phase

#SETTING UP DICTIONARY#
# if statement, conditional check to ensure 'weather_data' is not = null    
if weather_data:

    weather_description = weather_data['weather'][0]['description'] 
    temperature = round(weather_data['main']['temp'])
    feels_like = round(weather_data['main']['feels_like'])
    high = round(weather_data['main']['temp_max'])
    low = round(weather_data['main']['temp_min'])
    country = weather_data['sys']['country']

#BOOLEAN VALUES#

is_hot = temperature > 21
is_cold = temperature < 13
is_raining = 'rain' in weather_description.lower() # string slicing /inbuilt function 'lower()'

#STRING SLICING && DATETIME#
dt_object = datetime.now()
dt_string = str(dt_object)
dt_string_without_milliseconds = dt_string[:-7]
date = dt_string_without_milliseconds[:10]
time = dt_string_without_milliseconds[11:]

#OUTPUT#
print("---------------------------------------------------------")
print(f"The Weather Forecast for today: {date} in {location}:  ")
print(f"The weather in {location[0].upper()}{location[1:]} is {temperature}° C with {weather_description}.")
print(f"It feels like {feels_like}° C, currently at {time}")
print(f"The Country code is '{country}'")
print(f"Today's high is {high}° C and today's low is {low}° C.")

if is_hot:
    print("It's hot ☀️ Consider wearing light clothing and apply some suncream!!")
elif is_cold:
    print("It's cold 🥶 Bundle up and keep an eye on children and the elderly that they don't get cold!")
elif is_raining:
    print("It's raining ☔ Don't forget your umbrella and be careful when driving!")
else:
    print("Weather seems OK 🫡 Enjoy your day, perhaps get a coffee!")

#WRITING DATA TO JSON FILE#
filename = 'weather_data.txt' 
with open(filename, 'a') as file: 
    file.write(location) 
    file.write('\n')
    json.dump(weather_data, file) # 'json.dump() writes 'weather_data' dict to the file
    # cannot use typical file.write() as we want to write a dictionary to the file
    file.write('\n')  

print("---------------------------------------------------------")
print("Weather data has been written to: ", filename)
#in vscode we can see 'weather_data.txt' in the navigation pane
# if opened we can see the 'weather_data' in json format
print("---------------------------------------------------------")