# explain the difference between:
# from flask import Flask, render_template, and
# import requests
import requests
#the api endpoint we are going to request our data from
endpoint = "http://api.openweathermap.org/data/2.5/weather"
#the parameters we are going to pass to make the data we get back more specific
payload = {"q": "London,UK", "units":"metric", "appid":""}
#store the response of the actual get request
response = requests.get(endpoint, params=payload)

#the url we requested the data from
print response.url
#was the api request successful?
print response.status_code

print response.headers["content-type"]

#raw response
print response.text

#convert to json so we can access the data easily with name / value pairs
data = response.json()
print data

temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print u"It's {}C in {}, and the sky is {}".format(temperature, name, weather)