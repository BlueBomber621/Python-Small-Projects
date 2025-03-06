import requests

OWA_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY="Your API Key" 
lat=0
lon=0

OWA_params = {
    "appid": API_KEY,
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "units": "imperial",
}

response = requests.get(OWA_ENDPOINT, OWA_params)
response.raise_for_status()
data = response.json()

print(f"The current temp is {data['main']['temp']}°F and feels like {data['main']['feels_like']}°F. The current weather condition is: {data['weather'][0]['description']}. The humidity is {data['main']['humidity']}%, and the visibility is {data['visibility'] / 1000}km. The wind speed is {data['wind']['speed']}mi/hr at a {data['wind']['deg']}-degree angle.")