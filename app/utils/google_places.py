# Anything to do with Google Places API calls
from flask import jsonify
import requests

def places_query(query, api_key):
    # Google Places API url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Parameteres we pass into the GET request
    params = {'query': query, 'key': api_key}

    # Send GET request
    response = requests.get(url, params=params)

    # Check if response is code 200 OK
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return jsonify({'error': response.text}), response.status_code
