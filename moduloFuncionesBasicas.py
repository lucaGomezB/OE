import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')
#-----------------------------------------------------------
#                   FUNCIONES BÁSICAS
#-----------------------------------------------------------

def traductor(description):
    if description == "clear sky":
        description = "Cielo despejado"
    elif description == "few clouds":
        description = "Pocas nubes"
    elif description == "broken clouds":
        description = "Nubes despejadas"
    elif description == "scattered clouds":
        description = "Escazas Nubes"
    elif description == "overcast clouds":
        description = "Nublado"
    elif description == "light rain":
        description = "Lluvia ligera"
    return description

def get_current_weather(city, units='metric'):
    print()
    #Con esta función se obtiene el clima actual.
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + API_KEY + "&units=" + units
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        weather_desc = traductor(weather_desc)
        print(f"Ciudad: {city}")
        print(f"Descripción: {weather_desc}")
        print(f"Temperatura: {main['temp']}°")
        print(f"Humedad: {main['humidity']}%")
        print(f"Velocidad del viento: {wind['speed']} m/s")
        #Acá se muestran los datos
        return data
    else:
        print("Error en la consulta, por favor verifica el nombre de la ciudad.")
        return None
    

def get_forecast(city, units='metric'):
    print()
    #Esta función obtiene el pronóstico de los próximos 5 días.
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "q=" + city + "&appid=" + API_KEY + "&units=" + units
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        print(f"Pronóstico para los próximos 5 días en {city}:")
        for forecast in data['list']:
            date = forecast['dt_txt']
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"{date}: {temp}° - {traductor(description)}")
        return data
    else:
        print("Error en la consulta del pronóstico. Porfavor verifique la ciudad ingresada.")
        return None