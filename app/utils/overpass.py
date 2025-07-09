# Anything to do with overpass API calls
import requests

def restaurants(lat, lon, radius=1000):
    url = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    node(around:{radius},{lat},{lon})["amenity"="restaurant"];    
    out;
    """

    response = requests.post(url, data={'data': query})
    if response.ok:
        return response.json()['elements']
    else:
        return []