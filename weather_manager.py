import requests
from datetime import datetime

WEATHER_API_KEY = "{YOUR_WEATHER_API_KEY}"
WEATHER_ENDPOINT = "httpS://api.openweathermap.org/data/2.5/onecall"

class WeatherManager():
    def __init__(self, lat, lon, min_wind_speed):
        self.lat = lat
        self.lon = lon
        self.min_wind_speed = min_wind_speed

    def get_weather_data(self):
        weather_params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": WEATHER_API_KEY,
            "exclude": "current,minutely,hourly"
        }

        response = requests.get(WEATHER_ENDPOINT, params=weather_params)
        response.raise_for_status()
        data = response.json()['daily']
        return data


    def get_next_days_with_wind(self):
        weather_data = self.get_weather_data()
        days_with_wind = [(datetime.fromtimestamp(n['dt']).strftime('%d/%m'), n['wind_speed']) for n in weather_data if
                          n['wind_speed'] >= self.min_wind_speed]
        return days_with_wind

    def get_next_day_with_wind(self):
        result = None
        days_with_wind = self.get_next_days_with_wind()
        if len(days_with_wind) > 0:
            next_day_with_wind = days_with_wind[0][0]
            next_day_wind_speed = days_with_wind[0][1]
            result = (next_day_with_wind, next_day_wind_speed)
        return  result
