from django.shortcuts import render
from collections import defaultdict
from datetime import datetime
from django.conf import settings
import logging
logger=logging.getLogger('django')
import requests
# Create your views here.
def index(request):
    context = {}
    try:
        if request.method == 'POST':
            city = request.POST.get('city', 'Kathmandu').strip()
            if not city:
                city = 'Kathmandu'  # fallback
        else:
            city = 'Kathmandu'

        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}'
        url1=f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={settings.OPENWEATHER_API_KEY}'
        url2=f'https://api.unsplash.com/search/photos?query={city}&client_id={settings.UNSPLASH_API_KEY}'
        images = requests.get(url2,timeout=5).json()
        params={'units':'metric'}
        data = requests.get(url,params,timeout=5).json()
        popular = ['Kathmandu', 'New York', 'Tokyo', 'London']
        popular_data = []
        for city_name in popular:
            try:
                weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.OPENWEATHER_API_KEY}'
                image_url = f'https://api.unsplash.com/search/photos?query={city_name}&per_page=1&client_id={settings.UNSPLASH_API_KEY}'

                weather = requests.get(weather_url, params={'units': 'metric'}, timeout=5).json()
                image_data = requests.get(image_url, timeout=5).json()

                # Validate weather response
                if weather.get('cod') != 200 or 'main' not in weather or 'weather' not in weather:
                    logger.warning(f"Skipping {city_name}: Invalid weather data")
                    continue

                # Validate image response
                if not image_data.get('results'):
                    logger.info(f"Skipping {city_name}: No image found")
                    continue

                popular_data.append({
                    'city': city_name,
                    'temp': weather['main']['temp'],
                    'desc': weather['weather'][0]['description'],
                    'icon': weather['weather'][0]['icon'],
                    'image': image_data['results'][0]['urls']['regular']
                })

            except Exception as e:
                logger.error(f"Error fetching data for {city_name}: {e}", exc_info=True)
                continue
        error_message = None
        if str(data.get('cod')) != '200':
            error_message = data.get('message', 'Unknown error')
            temp = humidity = wind = desc = icon = pressure = visibility = None
            image = '/static/images/default.png'
            forecasts = []
        else:
            data1 = requests.get(url1,params,timeout=5).json()
            results = images.get('results') or []
            if results:
                image = results[0]['urls']['regular']
            else:
                image = '/static/images/default.png'
            temp = data['main']['temp']
            humidity = data['main']['humidity'] 
            wind = data['wind']['speed']
            desc = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            pressure = data['main']['pressure']
            visibility = data['visibility']
            
            daily_data = defaultdict(list)
            for entry in data1.get('list', []):
                date_str = entry['dt_txt'].split(' ')[0]
                entry_temp = entry['main']['temp']
                entry_icon = entry['weather'][0]['icon']
                daily_data[date_str].append({'temp': entry_temp, 'icon': entry_icon})
            forecasts = []
        
            for date, entries in daily_data.items():
                temps = [e['temp'] for e in entries]
                icons = [e['icon'] for e in entries]
                forecasts.append({
                    'day': datetime.strptime(date, '%Y-%m-%d').strftime('%A'),
                    'min_temp': int(min(temps)),
                    'max_temp': int(max(temps)),
                    'icon': icons[0]  # Just pick the first icon for simplicity
                })
   
        context={
            'error': error_message,
            'temp':temp,
            'city':city,
            'desc':desc,
            'icon':icon,
            'humidity':humidity,
            'wind':wind,
            'pressure':pressure,
            'visibility':visibility,
            'forecasts':forecasts,
            'image':image,
            'popular_cities': popular_data,
        }
    except Exception as e:
        logger.error(e, exc_info=True)
        context = {
            'error': "Something went wrong. Please try again later.",
            'city': "Kathmandu",
            'image': "/static/images/default.png",
            'popular_cities': [],
        }
    return render(request,'index.html',context)