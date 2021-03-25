import os
from dotenv import load_dotenv
load_dotenv()
from marinetrafficapi import MarineTrafficApi

api_key = os.environ['MARINE_TRAFFIC_API_KEY']
api = MarineTrafficApi(api_key=api_key)

vessel = api.single_vessel_positions(time_span=120, mmsi=353136000)

vessel = vessel.models[0]

latitude = vessel.latitude.value
longitude = vessel.longitude.value
speed = vessel.speed.value

stuck_latitude = 30.01765
stuck_longitude = 32.5802
stuck_speed = 0

if speed != stuck_speed and latitude != stuck_latitude and longitude != stuck_longitude:
    print("It's moving")
else:
    print("Still stuck")