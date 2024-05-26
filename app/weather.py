from flask import Blueprint, request, jsonify
from .utils import get_weather_data, format_json_response, format_xml_response

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/getCurrentWeather', methods=['GET'])
def get_current_weather():
    data = request.get_json()
    city = data.get("city")
    output_format = data.get("output_format", "json")

    if not city:
        return jsonify({"error": "City not provided"}), 400

    weather_data = get_weather_data(city)

    if output_format == "json":
        response_data = format_json_response(weather_data)
        return jsonify(response_data)
    elif output_format == "xml":
        response_data = format_xml_response(weather_data)
        return response_data, 200, {'Content-Type': 'application/xml'}
    else:
        return jsonify({"error": "Invalid output format"}), 400
