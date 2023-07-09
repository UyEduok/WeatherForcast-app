import requests
import os

API_KEY = os.environ.get('API_key')


def get_data(place, forcast_days, kind):

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    nr_days = 8*forcast_days
    filtered_content = filtered_content[:nr_days]
    if kind == 'Temperature':
        filtered_content = [dict['main']['temp'] for dict in filtered_content]
    if kind == 'Sky':
        filtered_content = [dict['weather'][0]['main'] for dict in filtered_content]
    return filtered_content

if __name__ == '__main__':
    print(get_data(place='Uyo', forcast_days=2, kind='Sky'))
