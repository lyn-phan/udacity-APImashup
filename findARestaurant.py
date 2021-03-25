import geocode
import json
import httplib2
import requests
import os

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = os.environ.get('CLIENT_ID')
foursquare_client_secret = os.environ.get('CLIENT_SECRET')

def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    latitude, longitude = getGeocodeLocation(location)
     #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

    # payload = {
    #     'll': 'latitude', 'longitude'
    #     'v': 20190425,
    #     'query': 'mealtype'
    # }

    # req = requests.get(f'https://api.foursquare.com/v2/venues/search?client_id={foursquare_client_id}&client_secret={foursquare_client_secret}', params=payload)


    url = (f"https://api.foursquare.com/v2/venues/search?client_id={foursquare_client_id}&client_secret={foursquare_client_secret}&v=20190425&{latitude}{longitude}&query={mealType}")
    h = httplib2.Http()
    # response, content = h.request(url, 'GET')
    # return response
    result = json.loads(h.request(url, 'GET')[1])


	# 3. Grab the first restaurant
    if result['response']['venues']:
        restaurant = result['response']['venues'][0]
        venue_id = restaurant['id']
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['formattedAddress']
        address = ''
        for i in restaurant_address:
            address += i + ''
        restaurant_address = address
    
    restaurantInfo = {'name':restaurant_name, 'address':restaurant_address}
    
    # print("Restaurant Name:" restaurant_name)
    # print("Address:" restaurant_address)
    return restaurantInfo


	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url	
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney, Australia")