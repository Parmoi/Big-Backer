from flask import Blueprint, current_app, jsonify, render_template, request, session

from app.utils import google_places, overpass

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/search')
def search():
    return render_template('search.html')

@main.route('/save_location', methods=['POST'])
def set_location():
    data = request.get_json()
    session['location'] = {
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }

    return jsonify({'status': 'success'})

@main.route('/get_location', methods=['GET'])
def get_location():
    location = session.get('location')
    lat = location['latitude']
    lon = location['longitude']

    if lat is not None and lon is not None:
        return jsonify({'latitude': lat, 'longitude': lon})
    else:
        return jsonify({'error': 'Location not set yet'}), 404
    
@main.route('/get_restaurants', methods=['GET'])
def get_restaurants():
    location = session.get('location')
    lat = location['latitude']
    lon = location['longitude']

    if not lat or not lon:
        return jsonify({'error': 'Missing coordinates'}), 400
    
    places = overpass.restaurants(lat, lon)
    return jsonify(places)

@main.route('/search_places', methods=['GET'])
def search_places():
    query = 'Ashfield restaurants'

    place_ids = google_places.find_place_ids(query, current_app.config['GOOGLE_PLACES_API_KEY'])

    place_details = google_places.find_detailed_places(place_ids, current_app.config['GOOGLE_PLACES_API_KEY'])

    return jsonify(place_details)