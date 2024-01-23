import requests

OWM_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

api_key = 'Get from the openweather map'

weather_params = {
    "lat": 17.385044,
    "lon": 78.486671,
    "appid": api_key
}

response = requests.get(OWM_endpoint, params=weather_params)
print(response.status_code)

weather_data = response.json()

#print(weather_data["list"][0]["weather"][0])

will_rain= False
for hour_data in weather_data["list"]:
    condition_codes = hour_data["weather"][0]["id"]
    if int(condition_codes) < 700:
        #print("Bring an Umberalla")
        will_rain = True

if will_rain:
    print("Bring an Umeralla")
    # Can use the Twilio APIs to send SMS
    # Use Python Anywhere to run your python code from any where.







