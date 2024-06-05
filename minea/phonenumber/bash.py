# phone_info.py

import phonenumbers
from phonenumbers import geocoder, timezone, carrier
from colorama import init, Fore
import folium
import os

init()

def get_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        info = {
            "formatted_number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "time_zone": timezone.time_zones_for_number(parsed_number),
            "region": geocoder.description_for_number(parsed_number, "fr"),
            "service_provider": carrier.name_for_number(parsed_number, 'fr')
        }
        print(info)
        return info
    except Exception:
        print(f"{Fore.RED}[-] Please specify a valid phone number (with country code) or check your internet connection.")
        return None

def draw_map(latitude, longitude, location, phone_number):
    try:
        my_map = folium.Map(location=[latitude, longitude], zoom_start=9)
        folium.Marker([latitude, longitude], popup=location).add_to(my_map)
        cleaned_phone_number = ''.join(char for char in phone_number if char.isdigit() or char == '+')
        file_name = f"{cleaned_phone_number}.html"
        my_map.save(file_name)
        print(f"[+] See Aerial Coverage at: {os.path.abspath(file_name)}")
    except NameError:
        print(f"{Fore.RED}[-] Could not get Aerial coverage for this number. Please check the number again.")
