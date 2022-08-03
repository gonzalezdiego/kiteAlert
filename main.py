from notification_manager import NotificacionManager
from weather_manager import  WeatherManager

LAT= "{YOUR_CITY_LAT}"
LON = "{YOUR_CITY_LON}"
MIN_WIND_SPEED = "{YOUR_MIN_WIND_SPEED}"
TO_PHONENUMBER = "{YOUR_PHONE_NUMBER}"

wm = WeatherManager(lat=LAT, lon=LON, min_wind_speed=MIN_WIND_SPEED)
next_day_with_wind = wm.get_next_day_with_wind()

if next_day_with_wind is not None:
    nm = NotificacionManager()
    message = nm.format_message(next_day_with_wind[0], next_day_with_wind[1])
    nm.send_message(message=message, to_number=TO_PHONENUMBER)
