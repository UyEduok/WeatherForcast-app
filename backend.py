import requests
import os

API_KEY = os.environ.get('API_KEY')


def get_data(place, forcast_days):

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    nr_days = 8*forcast_days
    filtered_content = filtered_content[:nr_days]
    return filtered_content



