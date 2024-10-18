import requests
from dotenv import load_dotenv
load_dotenv()
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#Acá se importa lo que usaremos

API_KEY = os.getenv('API_KEY')
#Con esto accedemos a la API

#Primero hay que definir las funciones que vamos a usar : 


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

#-----------------------------------------------------------
#                 FUNCIONES GRÁFICAS FRONT
#-----------------------------------------------------------

def show_weather():
    city = city_entry.get()
    if city:
        result = get_current_weather(city, units_var.get())
        result_label.config(text=result)
    else:
        messagebox.showwarning("Input Error", "Por favor ingresa el nombre de la ciudad")

def show_forecast():
    city = city_entry.get()
    if city:
        result = get_forecast(city, units_var.get())
        result_label.config(text=result)
    else:
        messagebox.showwarning("Input Error", "Por favor ingresa el nombre de la ciudad")

def change_units():
    if units_var.get() == 'metric':
        units_var.set('imperial')
    else:
        units_var.set('metric')
    units_button.config(text=f"Unidades: {units_var.get()}")

#--------------------------------------------------------------
#                   FUNCIONES GRAFICAS BACK
#--------------------------------------------------------------

#--------------------------------------------------------------------------------------

# Crear ventana principal
root = tk.Tk()
root.title("Aplicación del Clima")

# Cargar la imagen de fondo
try:
  background_image = Image.open("app/8.jpg") 
  background_photo = ImageTk.PhotoImage(background_image)
except FileNotFoundError:
  background_color = "#37bfbb"  # Replace with your desired background color

# Crear un canvas para colocar la imagen de fondo
canvas = tk.Canvas(root, width=background_image.width, height=background_image.height)
canvas.grid(row=0, column=0, columnspan=2)  # Expandir en dos columnas

# Colocar la imagen en el canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Etiqueta y campo de texto para ingresar ciudad
city_label = tk.Label(root, text="Ciudad:", bg="white")
city_label_window = canvas.create_window(10, 10, anchor="nw", window=city_label)

city_entry = tk.Entry(root)
city_entry_window = canvas.create_window(80, 10, anchor="nw", window=city_entry)

# Botón para consultar el clima actual
current_weather_button = tk.Button(root, text="Clima Actual", command=show_weather)
current_weather_button_window = canvas.create_window(10, 50, anchor="nw", window=current_weather_button)

# Botón para consultar el pronóstico
forecast_button = tk.Button(root, text="Pronóstico a 5 días", command=show_forecast)
forecast_button_window = canvas.create_window(10, 90, anchor="nw", window=forecast_button)

# Botón para cambiar las unidades (Celsius/Fahrenheit)
units_var = tk.StringVar(value='metric')
units_button = tk.Button(root, text=f"Unidades: {units_var.get()}", command=change_units)
units_button_window = canvas.create_window(10, 130, anchor="nw", window=units_button)

# Etiqueta para mostrar los resultados
result_label = tk.Label(root, text="", justify="left", bg="white")
result_label_window = canvas.create_window(10, 170, anchor="nw", window=result_label)

# Ejecutar el loop principal de Tkinter
root.mainloop()