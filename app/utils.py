import requests
import os
from xml.etree.ElementTree import Element, SubElement, tostring

RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
WEATHER_API_URL = "https://weatherapi-com.p.rapidapi.com/current.json"

def get_weather_data(city):
    querystring = {"q": city}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(WEATHER_API_URL, headers=headers, params=querystring)
    return response.json()

def format_json_response(weather_data):
    return {
        "Weather": weather_data["current"]["temp_c"],
        "Latitude": weather_data["location"]["lat"],
        "Longitude": weather_data["location"]["lon"],
        "City": f"{weather_data['location']['name']}, {weather_data['location']['country']}"
    }

def format_xml_response(weather_data):
    root = Element("root")
    temperature = SubElement(root, "Temperature")
    temperature.text = str(weather_data["current"]["temp_c"])
    city = SubElement(root, "City")
    city.text = weather_data["location"]["name"]
    latitude = SubElement(root, "Latitude")
    latitude.text = str(weather_data["location"]["lat"])
    longitude = SubElement(root, "Longitude")
    longitude.text = str(weather_data["location"]["lon"])
    return tostring(root, encoding="unicode")
