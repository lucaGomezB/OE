import tkinter as tk
from PIL import Image, ImageTk
import moduloFuncionesGraficasFront
import os
#--------------------------------------------------------------
#                   FUNCIONES GRAFICAS BACK
#--------------------------------------------------------------

#--------------------------------------------------------------------------------------

# Crear ventana principal
display_value = os.environ.get('DISPLAY')
if (display_value is None): 
  pass
else:
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
  current_weather_button = tk.Button(root, text="Clima Actual", command=moduloFuncionesGraficasFront.show_weather)
  current_weather_button_window = canvas.create_window(10, 50, anchor="nw", window=current_weather_button)

  # Botón para consultar el pronóstico
  forecast_button = tk.Button(root, text="Pronóstico a 5 días", command=moduloFuncionesGraficasFront.show_forecast)
  forecast_button_window = canvas.create_window(10, 90, anchor="nw", window=forecast_button)

  # Botón para cambiar las unidades (Celsius/Fahrenheit)
  units_var = tk.StringVar(value='metric')
  units_button = tk.Button(root, text=f"Unidades: {units_var.get()}", command=moduloFuncionesGraficasFront.change_units)
  units_button_window = canvas.create_window(10, 130, anchor="nw", window=units_button)

  # Etiqueta para mostrar los resultados
  result_label = tk.Label(root, text="", justify="left", bg="white")
  result_label_window = canvas.create_window(10, 170, anchor="nw", window=result_label)