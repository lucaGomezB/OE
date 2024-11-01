from datetime import datetime
import requests
from dotenv import load_dotenv
import os
from collections import defaultdict
load_dotenv()
API_KEY = os.getenv('API_KEY')
#
iconos_clima = {
    "clear sky": "☀️",
    "few clouds": "🌤️",
    "scattered clouds": "⛅",
    "overcast clouds": "☁️",
    "light rain": "🌧️",
    "rain": "🌧️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️"
}

#-----------------------------------------------------------
#                   FUNCIONES BÁSICAS
#-----------------------------------------------------------
def imprimir_recuadro(titulo, contenido):
    ancho = max(len(titulo), max(len(linea) for linea in contenido)) + 4
    print("+" + "-" * ancho + "+")
    print(f"| {titulo.center(ancho - 2)} |")
    print("+" + "-" * ancho + "+")
    for linea in contenido:
        print(f"| {linea.ljust(ancho - 2)} |")
    print("+" + "-" * ancho + "+\n")

def traductor(description):
    traducciones = {
        "clear sky": "Cielo despejado",
        "few clouds": "Pocas nubes",
        "scattered clouds": "Nubes dispersas",
        "overcast clouds": "Nublado",
        "light rain": "Lluvia ligera",
        "rain": "Lluvia",
        "thunderstorm": "Tormenta",
        "snow": "Nieve",
        "mist": "Niebla"
    }
    return traducciones.get(description, description)

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
        icono_clima = iconos_clima.get(weather_desc)
        weather_desc = traductor(weather_desc)
        if units == 'imperial':
            wind_speed_unit = "millas/s"
        else:
            wind_speed_unit = "metros/s"
        print(f"Ciudad: {city}")
        print(f"Descripción: {weather_desc} {icono_clima}")
        print(f"Temperatura: {main['temp']}°")
        print(f"Humedad: {main['humidity']}%")
        print(f"Velocidad del viento: {wind['speed']} {wind_speed_unit}")
        #Acá se muestran los datos
        print("")
        return data
    else:
        print("Error en la consulta, por favor verifica el nombre de la ciudad.")
        print("")
        return None
    

def get_forecast(city, units='metric'):
    print()
    #Esta función obtiene el pronóstico de los próximos 5 días.
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "q=" + city + "&appid=" + API_KEY + "&units=" + units
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        forecast_by_day = defaultdict(list)
        for forecast in data['list']:
            date = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
            day = date.strftime('&Y-&m-%d')
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            feels_like = forecast['main']['feels_like']
            humidity = forecast['main']['humidity']
            description = forecast['weather'][0]['description']
            icon = forecast['weather'][0]['icon']
            forecast_by_day[day].append({
                'temp': temp,
                'feels_like': feels_like,
                'humidity': humidity,
                'description': description,
                'icon': icon,
                'date': date
            })
        print(f"Pronóstico para los próximos 5 días en {city}:")
        print('')
        for day, forecasts in forecast_by_day.items():
            temps = [f['temp'] for f in forecasts]
            feels_likes = [f['feels_like'] for f in forecasts]
            humidities = [f['humidity'] for f in forecasts]
            descriptions = [f['description'] for f in forecasts]
            min_temp = min(temps)
            max_temp = max(temps)
            min_feels_like = min(feels_likes)
            max_feels_like = max(feels_likes)
            avg_humidity = sum(humidities) / len(humidities)
            wind = data['wind']
            most_common_desc = max(set(descriptions), key=descriptions.count)
            readable_date = forecasts[0]['date'].strftime('%d %B')
            icono_clima = iconos_clima.get(most_common_desc, "")
            if units == 'imperial':
                wind_speed_unit = "millas/s"
            else:
                wind_speed_unit = "metros/s"
            print(f"{readable_date.capitalize()} {icono_clima}:") 
            print(f"  Temperatura mínima: {min_temp}°C (Sensación: {min_feels_like}°C)")
            print(f"  Temperatura máxima: {max_temp}°C (Sensación: {max_feels_like}°C)")
            print(f"  Humedad promedio: {avg_humidity:.1f}%")
            print(f"  Clima: {traductor(most_common_desc)}\n")
            print(f"Velocidad del viento: {wind['speed']} {wind_speed_unit}")
        return data
    else:
        print("Error en la consulta del pronóstico. Porfavor verifique la ciudad ingresada.")
        print("")
        return None
    
def menu(contador):
    #Esta función se usa como menú interactivo. 
    historial = []
    contador = contador + 1 
    if contador == 1:
        unidad = 'metric'
    while True:
        imprimir_recuadro("Menú", [
            "1. Consultar el clima actual",
            "2. Ver pronóstico para los próximos 5 días",
            "3. Cambiar unidades (Celsius/Fahrenheit)",
            "4. Ver historial de consultas",
            "5. Salir"
        ])
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            ciudad = input("Ingresa el nombre de la ciudad: ")
            get_current_weather(ciudad, unidad)
            historial.append(ciudad)
        elif opcion == '2':
            ciudad = input("Ingresa el nombre de la ciudad: ")
            get_forecast(ciudad, unidad)
            historial.append(ciudad)
        elif opcion == '3':
            while True: 
                unidad = input("Selecciona las unidades ( metric (Cº) | imperial (Fº)): ")
                if unidad in ['metric', 'imperial','Metric','Imperial','METRIC','IMPERIAL']:
                    print(f"Unidades cambiadas a {unidad}.")
                    print("")
                    break
                else:
                    print("Opción inválida.")
                    print('')
        elif opcion == '4':
            print("Historial de consultas:")
            for ciudad in historial:
                print(ciudad)
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
            print('')