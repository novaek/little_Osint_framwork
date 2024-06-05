# main.py
from phonenumber.bash import get_info, draw_map
from opencage.geocoder import OpenCageGeocode

def get_coordinates(location):
    coder = OpenCageGeocode("YOUR_API_KEY")  # Replace with your actual OpenCage API key
    results = coder.geocode(location)
    if results:
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        return latitude, longitude
    else:
        return None, None

def main(phone_number):
    info = get_info(phone_number)
    if info and info['region']:
        latitude, longitude = get_coordinates(info['region'])
        if latitude and longitude:
            draw_map(latitude, longitude, info['region'], phone_number)
        else:
            print(f"[-] Could not determine coordinates for region: {info['region']}")
    else:
        print(f"[-] Could not retrieve information for phone number: {phone_number}")


