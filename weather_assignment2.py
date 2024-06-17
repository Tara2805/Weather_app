import requests
import json
from datetime import datetime 

api_key = ''

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
while True: # using while loop, if user input = true / using boolean
    location = input("Hi please input a Location: ") # asks for user to input a location /inbuilt function 'input()'
    location = location.capitalize()  # Capitalize the first letter /inbuilt function 'capitalize()'
    #calls weather function with provided api key && user inputted location
    weather_data = get_weather(api_key, location) # stores both in the variable 'weather_data'
    if weather_data: # if statement, testing if weather data is not null
        break # if weather data valid = break loop and go to next phase

#SETTING UP DICTIONARY#
# if statement, conditional check to ensure 'weather_data' is not = null    
if weather_data:
    # 'weather_description' accesses the 'weather' key in the weather_data dictionary, which contains a list of weather descriptions
    weather_description = weather_data['weather'][0]['description'] #'[0]' is used to select the first (main) weather condition
    # 'temperature' accesses the 'main' key in the 'weather_data' dictionary, which contains other main weather parameters
    temperature = round(weather_data['main']['temp']) # round the temperature to the nearest whole number /inbuilt function 'round()'
    # 'feels_like' extracts the 'feels_like' temperature from the main weather parameters
    feels_like = round(weather_data['main']['feels_like'])
    # 'high' extracts the maximum temperature from the main weather parameters
    high = round(weather_data['main']['temp_max'])
    # 'low' extrats the minimum temperature from the main weather parameters
    low = round(weather_data['main']['temp_min'])
    # 'country' extracts the country code from 'sys' 
    country = weather_data['sys']['country']

#BOOLEAN VALUES#

is_hot = temperature > 21
is_cold = temperature < 13
# Determine if it's raining based on weather description from the dict
is_raining = 'rain' in weather_description.lower() # string slicing /inbuilt function 'lower()'

#STRING SLICING && DATETIME#
# 'dt_object' is using the build in function 'datetime.now()' from the module 'datetime' that we imported earlier
# This allows us to get the current datetime that we are making the location request at
dt_object = datetime.now()
# Convert the datetime object to a string so we can use string slicing
dt_string = str(dt_object)
# Remove the last 7 characters using string slicing, as the milliseconds are not needed
dt_string_without_milliseconds = dt_string[:-7]
# now split using string slicing into a separate date and time
# using string slicing remove the last 10 digits so we just get the date
date = dt_string_without_milliseconds[:10]
# using string slicing remove the first 11 digits so we just get the time
time = dt_string_without_milliseconds[11:]

#OUTPUT#
print("---------------------------------------------------------")
# based on user input and the weather dictionary, output the necessary data 
print(f"The Weather Forecast for today: {date} in {location}:  ")
print(f"The weather in {location[0].upper()}{location[1:]} is {temperature}° C with {weather_description}.")
print(f"It feels like {feels_like}° C, currently at {time}")
print(f"The Country code is '{country}'")
print(f"Today's high is {high}° C and today's low is {low}° C.")

# Providing recommendations based on weather conditions
#if else statement
if is_hot:
    print("It's hot ☀️ Consider wearing light clothing and apply some suncream!!")
elif is_cold:
    print("It's cold 🥶 Bundle up and keep an eye on children and the elderly that they don't get cold!")
elif is_raining:
    print("It's raining ☔ Don't forget your umbrella and be careful when driving!")
else:
    print("Weather seems OK 🫡 Enjoy your day, perhaps get a coffee!")

#WRITING DATA TO JSON FILE#
# import json module is needed for this to work /see 'import json' at top 
filename = 'weather_data.txt'  # defining variable 'filename' where 'weather_data' will be written
with open(filename, 'a') as file: # opens 'filename' 'with' means it will close after/ intends to write 'w'/ file object assigned to variable 'file' 
    file.write(location) # adding user inputted location to start of dictionary
    file.write('\n') # each new location weathers data will be on  a new line when ran
    json.dump(weather_data, file) # 'json.dump() writes 'weather_data' dict to the file
    # cannot use typical file.write() as we want to write a dictionary to the file
    file.write('\n')  

print("---------------------------------------------------------")
print("Weather data has been written to: ", filename) # outputs to console after writting to 'filename'
#in vscode we can see 'weather_data.txt' in the navigation pane
# if opened we can see the 'weather_data' in json format
print("---------------------------------------------------------")