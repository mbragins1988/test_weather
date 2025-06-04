# test_weather

### Описание 
Web-приложение для просмотра прогноза погоды на 10 дней.

### Как запустить проект

Клонировать репозиторий:

```
git clone git@github.com:mbragins1988/Yatube.git
```

Перейти в папку

```
cd Yatube
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

Перейти в папку yatube:

```
cd yatube
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

Перейти по адресу - http://127.0.0.1:8000

Создать суперпользователя

```
python3 manage.py createsuperuser
```

Адрес админ-панели - http://127.0.0.1:8000/admin

### Стек технологий:
- Python 3.7
- Django 2.2.16

### Авторы проекта
Михаил Брагин
