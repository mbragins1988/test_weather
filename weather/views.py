import requests
from django.shortcuts import render
from weather.forms import Add_cityForm


def form(request):
    """ Форма выбора страны и города."""

    # Коды погоды Open-Meteo и их описания
    weather_codes = {
        0: 'Ясно',
        1: 'Преимущественно ясно',
        2: 'Переменная облачность',
        3: 'Пасмурно',
        45: 'Туман',
        48: 'Туман с инеем',
        51: 'Морось: слабая',
        53: 'Морось: умеренная',
        55: 'Морось: сильная',
        56: 'Ледяная морось: слабая',
        57: 'Ледяная морось: сильная',
        61: 'Дождь: слабый',
        63: 'Дождь: умеренный',
        65: 'Дождь: сильный',
        66: 'Ледяной дождь: слабый',
        67: 'Ледяной дождь: сильный',
        71: 'Снег: слабый',
        73: 'Снег: умеренный',
        75: 'Снег: сильный',
        77: 'Снежные зерна',
        80: 'Ливень: слабый',
        81: 'Ливень: умеренный',
        82: 'Ливень: сильный',
        85: 'Снегопад: слабый',
        86: 'Снегопад: сильный',
        95: 'Гроза',
        96: 'Гроза со слабым градом',
        99: 'Гроза с сильным градом'
    }

    if request.POST:
        form = Add_cityForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['country']  # Получаем название страны из формы
            city = form.cleaned_data['city']  # Получаем название города из формы
            geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&country={country}&count=1"
            geo_response = requests.get(geocoding_url)
            geo_data = geo_response.json()

            if not geo_data.get('results'):

                context = {
                'error': 'Город не найден. Проверьте название и страну.'
                }
                return render(request, 'choice_city.html', context=context)
            
            location = geo_data['results'][0]
            latitude = location['latitude']
            longitude = location['longitude']
            
            # Получаем прогноз погоды
            weather_url = (
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={latitude}&longitude={longitude}"
                f"&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum"
                f"&timezone=auto&forecast_days=10"
            )
            
            response = requests.get(weather_url)
            data_city = {} # Данные города
            forecast = {} # Прогноз на 10 дней
            weatherdecode = [] # Декодированная погода\осадки
            weather_code_forecast = response.json().get('daily').get('weathercode')
            for code in weather_code_forecast:
                weatherdecode.append(weather_codes.get(code))

            temperature_type = response.json().get('daily_units').get('temperature_2m_max')
            forecast['time'] = response.json().get('daily').get('time')
            forecast['weathercode'] = weatherdecode
            forecast['temperature_max'] = response.json().get('daily').get('temperature_2m_max')
            forecast['temperature_min'] = response.json().get('daily').get('temperature_2m_min')
            data_city['country'] = location.get('country')
            data_city['name'] = location.get('name')
            data_city['latitude'] = latitude
            data_city['longitude'] = longitude

            context = {
                'title': 'Введите город',
                'form': form,
                'temperature_type': temperature_type,
                'forecast': forecast,
                'data_city': data_city,

            }
            return render(request, 'index.html', context=context)
    
    form = Add_cityForm()
    context = {
    'title': 'Выберите город',
    'form': form,
    }
    return render(request, 'choice_city.html', context=context)
