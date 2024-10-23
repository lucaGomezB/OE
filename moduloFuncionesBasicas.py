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
    
def menu():
    #Esta función se usa como menú interactivo. 
    historial = []
    while True:
        print("\nMenú:")
        print("1. Consultar el clima actual")
        print("2. Ver pronóstico para los próximos 5 días")
        print("3. Cambiar unidades (Celsius/Fahrenheit)")
        print("4. Ver historial de consultas")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            ciudad = input("Ingresa el nombre de la ciudad: ")
            get_current_weather(ciudad)
            historial.append(ciudad)
        elif opcion == '2':
            ciudad = input("Ingresa el nombre de la ciudad: ")
            get_forecast(ciudad)
            historial.append(ciudad)
        elif opcion == '3':
            unidad = input("Selecciona las unidades ( metric (Cº) | imperial (Fº)): ")
            if unidad in ['metric', 'imperial']:
                print(f"Unidades cambiadas a {unidad}.")
            else:
                print("Opción inválida.")
        elif opcion == '4':
            print("Historial de consultas:")
            for ciudad in historial:
                print(ciudad)
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intenta de nuevo.")