#!/usr/bin/env python

# This script will pull weather data and post the specified contents to a Spark room

import urllib2
import json

# You will need to request a Key ID from Weather Underground
# Make sure to set the location you wish to use for weather.  Not everyone cares about the weather in RTP, NC.
# https://www.wunderground.com/weather/api/
f = urllib2.urlopen('http://api.wunderground.com/api/<Your Key ID>/geolookup/conditions/q/NC/Research_Triangle_Park.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
humidity = parsed_json['current_observation']['relative_humidity']
feelslike_f = parsed_json['current_observation']['feelslike_f']
weather = parsed_json['current_observation']['weather']
weather_out = "The current weather in %s is: %sF with a Relative Humidity of %s. It feels like %sF and %s" % (location, temp_f, humidity, feelslike_f, weather)
f.close()

# You'll need to have your Spark Authentication Token and put itin the Authorization Header
# https://dev-preview.ciscospark.com/getting-started.html
request_headers = {
    "Authorization": "Bearer <Your Token>",
    "Content-Type": "application/json"
}

# Set your Spark Room ID that you wish to post to. You'll need to have rights to that room.
# https://dev-preview.ciscospark.com/endpoint-rooms-roomId-put.html
data = {
    "roomId" : "<Your Room ID>",
    "text" : weather_out,
}

req = urllib2.Request('https://api.ciscospark.com/v1/messages', headers=request_headers)

response = urllib2.urlopen(req, json.dumps(data))
