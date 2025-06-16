from flask import Blueprint, jsonify, render_template, request, session

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/save_location', methods=['POST'])
def set_location():
    data = request.get_json()
    session['location'] = {
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }

    return jsonify({'status': 'success'})