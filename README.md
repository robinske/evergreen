# Evergreen

["The Ever Given is very big and very stuck."](https://www.theatlantic.com/technology/archive/2021/03/were-going-to-need-a-smaller-boat/618414/)

There's also an [API for that](https://www.marinetraffic.com/). Tracking it, not [moving it](https://twitter.com/kelleyrobinson/status/1375172382076375048).

To run this:
1. Sign up for an API key here: https://www.marinetraffic.com/
2. Clone this repo: `git clone git@github.com:robinske/evergreen.git`
3. Create a `.env` file
4. Add the line: `MARINE_TRAFFIC_API_KEY='api key from step 1 here'`
5. Create a virtual environment `python -m venv venv`
6. Activate the virtual environment `source venv/bin/activate`
7. Install the dependencies: `pip install -r requirements.txt`
8. Run the code: `flask run`

[http://localhost:5000/boat](http://localhost:5000/boat)
