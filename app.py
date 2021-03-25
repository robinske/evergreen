import os
from dotenv import load_dotenv
load_dotenv()
from marinetrafficapi import MarineTrafficApi
from flask import Flask, Response

api_key = os.environ['MARINE_TRAFFIC_API_KEY']
api = MarineTrafficApi(api_key=api_key)

app = Flask(__name__)

@app.route('/boat', methods=["GET","POST"])
def boat():
    vessel = api.single_vessel_positions(time_span=120, mmsi=353136000)

    vessel = vessel.models[0]

    latitude = vessel.latitude.value
    longitude = vessel.longitude.value
    speed = vessel.speed.value

    stuck_latitude = 30.01765
    stuck_longitude = 32.5802
    stuck_speed = 0

    if speed != stuck_speed and latitude != stuck_latitude and longitude != stuck_longitude:
        return Response("""<Response><Message>It's moving!</Message></Response>""", mimetype="text/xml")
    else:
        return Response("""<Response><Message>Still stuck 😔</Message></Response>""", mimetype="text/xml")