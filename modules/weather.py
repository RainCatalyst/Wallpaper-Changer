import sys
sys.path.append("..")
import pyowm
import config

OpenWMap = pyowm.OWM(config.API_KEY)
Manager = OpenWMap.weather_manager()

def get_temperature(city_name):
    Weather = Manager.weather_at_place(city_name).weather
    return  Weather.temperature('celsius')['temp']