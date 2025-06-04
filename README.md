# test_weather

### Описание 
Web-приложение для просмотра прогноза погоды на 10 дней. Необходимо ввести страну, город и нажать кнопку "Узнать прогноз". Загрузиться прогноз погоды, в котором указывается страна, город, координаты, максимальная, минимальная температура воздуха и осадки. Используется бесплатное api open-meteo.com, поэтому некоторые города не ищутся :).

### Как запустить проект

Клонировать репозиторий:

```
git clone git@github.com:mbragins1988/test_weather.git
```

Перейти в папку

```
cd test_weather
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
для Windows
```
source venv/Scripts/activate
```
для Mac
```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip3 install -r requirements.txt
```

Перейти в папку test_weather:

```
cd test_weather
```

Выполнить миграции

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Запустить локальный сервер

```
python manage.py runserver
```

Перейти по адресу - http://127.0.0.1:8000/weather/

Создать суперпользователя

```
python3 manage.py createsuperuser
```

Адрес админ-панели - http://127.0.0.1:8000/admin

### Стек технологий:
- Python 3.8.10
- Django 4.2.21

### Авторы проекта
Михаил Брагин
