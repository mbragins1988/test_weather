from django.urls import path

from weather.views import form

app_name = 'weather'

urlpatterns = [
     path('', form, name='form'),
]
