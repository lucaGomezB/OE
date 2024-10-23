import moduloFuncionesBasicas
import moduloFuncionesGraficasBack
from tkinter import messagebox
#-----------------------------------------------------------
#                 FUNCIONES GRÁFICAS FRONT
#-----------------------------------------------------------

def show_weather():
    city = moduloFuncionesGraficasBack.city_entry.get()
    if city:
        result = moduloFuncionesBasicas.get_current_weather(city, moduloFuncionesGraficasBack.units_var.get())
        moduloFuncionesGraficasBack.result_label.config(text=result)
    else:
        messagebox.showwarning("Input Error", "Por favor ingresa el nombre de la ciudad")

def show_forecast():
    city = moduloFuncionesGraficasBack.city_entry.get()
    if city:
        result = moduloFuncionesBasicas.get_forecast(city, moduloFuncionesGraficasBack.units_var.get())
        moduloFuncionesGraficasBack.result_label.config(text=result)
    else:
        messagebox.showwarning("Input Error", "Por favor ingresa el nombre de la ciudad")

def change_units():
    if moduloFuncionesGraficasBack.units_var.get() == 'metric':
        moduloFuncionesGraficasBack.units_var.set('imperial')
    else:
        moduloFuncionesGraficasBack.units_var.set('metric')
    moduloFuncionesGraficasBack.units_button.config(text=f"Unidades: {moduloFuncionesGraficasBack.units_var.get()}")