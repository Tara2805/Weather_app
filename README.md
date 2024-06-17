# Weather_app
My first time working with APIs! I have created a console app, that asks for a user input and returns the current weather in your city!

Assignment 2 of the CFG degree

#IMPORTS#
Important!!! in order for this module to work follow these instructions
Open and then navigate to a terminal
In your terminal write and run the command 'pip install requests'
If successful this module and its dependencies will be installed and this command will work
If unsuccessful ensure you have Python's package manager pip installed on your system
Importing requests module which allows us to send HTTP requests
Part of Python's standard library, no install necessary for json
Provides functions for encoding Python objects into JSON strings
Importing from 'datetime' allows us to directly access the 'datetime' class without qualifying it
this means when calling later we use datetime.now() instead of datetime.datetime.now()

#API KEYS#
It is used for authentication when making requests to the OpenWeatherMap API
In order to set up an API key you must first navigate to the APIs website and sign up
weatherAPI sign up = https://home.openweathermap.org/users/sign_in
Once signed up we can see, copy and generate API keys
Enter the key that was sent to you in the variable "api_key"

api_key is used as a parameter in the URL when making a request to the OpenWeatherMap API
Do not publically share your API keys, this can be a security risk to your sensitive data