from flask import Blueprint, current_app, jsonify, render_template, request, session

from app import db
from app.models import Store

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

    place_ids = google_places.find_place_ids(current_app.config['GOOGLE_PLACES_API_KEY'], query, 4.0)

    place_details = google_places.find_detailed_places(place_ids, current_app.config['GOOGLE_PLACES_API_KEY'])

    return jsonify(place_details)

@main.route('/find_filtered_places', methods=['POST'])
def find_filtered_places():
    data = request.get_json()
    query = data.get("query")
    rating = float(data.get("min_rating"))  # Optional if you want to use it
    open_time = data.get("open_time")  # Optional
    close_time = data.get("close_time")  # Optional

    # You can build a more specific query using rating/open_time/close_time if needed
    place_ids = google_places.find_place_ids(current_app.config['GOOGLE_PLACES_API_KEY'], query, rating)

    return jsonify({"place_ids": place_ids})

@main.route('/add')
def add():
    new_store = Store(id='abcdef', name='random store')
    db.session.add(new_store)
    db.session.commit()

    # For testing purposes, I want to print the table I just added to
    # Equivalent to SELECT * FROM user
    # stores = Store.query.all()
    # print(stores)

    return jsonify({'result': 'its okay!'})

@main.route('/find_stores')
def find_stores():
    # Equivalent to SELECT * FROM user
    stores = Store.query.all()

    json_data = [store.to_dict() for store in stores]
    return jsonify(json_data)