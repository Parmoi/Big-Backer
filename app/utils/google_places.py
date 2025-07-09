# Anything to do with Google Places API calls
from flask import jsonify
import requests

# Takes in a query and returns a list of place_id's from our query
def find_place_ids(query, api_key):
    # Google Place Text Search API url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Parameters we pass into the GET request
    params = {'key': api_key, 'query': query, 'opennow': 'true', 'type': 'restaurant'}

    # Send GET request
    response = requests.get(url, params=params)

    # Check if response is code 200 OK
    if response.status_code == 200:
        # return [place['place_id'] for place in response.json().get('results', [])]

        # Only returning one place_id for now since I don't want the API call to be expensive
        return [response.json().get('results', [])[0]['place_id']]

    else:
        'Invalid'

# Takes in a list of place_ids and finds their important details
def find_detailed_places(place_ids, api_key):
    # Google Place Detail url
    url = "https://maps.googleapis.com/maps/api/place/details/json"

    # Loop each place and find their details
    for place_id in place_ids:
        print(place_id)
        # Parameters we pass into the GET request
        params = {'fields': 'name', 'key': api_key, 'place_id': place_id}

        # Send GET request
        response = requests.get(url, params=params)

        # Check if response is code 200 OK
        if response.status_code == 200:
            return response.json().get('result', [])
        else:
            return 'Invalid'