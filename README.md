# Weather API
This assignment contains a flask app for fetching weather data for a city with data format.
Below are the steps for running the app:
- Run `pip install -r requirements.txt`
- Run `python run.py`
- Run `curl --location --request GET 'http://127.0.0.1:5000/getCurrentWeather' \
--header 'Content-Type: application/json' \
--data '{
  "city":"Bangalore",
  "output_format": "json"
}'`
- You should see the json.
- Profit!!!
