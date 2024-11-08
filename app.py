from dotenv import load_dotenv
import os
load_dotenv()
#Acá se importa lo que usaremos

API_KEY = os.getenv('API_KEY')
#Con esto accedemos a la API

#Primero, se importa moduloFuncionesBasicas, que deja correr el programa incluso cuando no se tiene cabeza.
import moduloFuncionesBasicas
#Luego, se ejecuta el programa por consola. Decidimos dejar de lado el soporte para gráficos avanzados.
moduloFuncionesBasicas.menu()
