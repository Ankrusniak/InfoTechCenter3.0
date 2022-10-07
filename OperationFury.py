#Weather
#Developer:Andrew Krusniak
#version 1.0

"""
Create a function for our current weather using the 
random.choice function to determine what the weather is 
picking from a list-using a If,elif & E;se statements 
to check the condition and print a specific print line
"""

#Import Libraries here
import random
#Weather condition list using the random.choic library
#to randomly choos a condition and storing it in its brain
def weather():
    weather_forcast = ["Rain","Snow","Sunny","Cloudy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weather_forcast)
    return weatherCondition
weatherAlert = weather()
def vrs():
    if weather() == "Icy":
        print("\nvrs has changed your alarm 30 minutes earlier based on the NWS forcast of "+weatherAlert)

vrs()
