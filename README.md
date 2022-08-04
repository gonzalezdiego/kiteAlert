# KiteAlert
KiteAlert is a Python script to send a sms when next days wind conditions are more than X nots value.

## How to use this? 
1- Create a free Twilio account and replace SID, TOKEN, FROM_NUMBER on notification_manager.py file. Also add the number that you want to recibe the sms on Twilio. 

2- Create a free OpenWeather account and replace API_KEY on weather_manager.py file 

3- Verify the latitude and longitud of the city you want and replace LAT and LON on main.py

4- Update MIN_WIND_SPEED value on main.py

5- Create an account on pythonanyware.com, upload all these files and create a task to run on a daily basis.

## Built with

Language: Python

Apis: OpenWeatherApi, Twilio

Host: PythonAnywhere

