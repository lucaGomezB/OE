from dotenv import load_dotenv
import os
load_dotenv()
#Acá se importa lo que usaremos

API_KEY = os.getenv('API_KEY')
#Con esto accedemos a la API

#Primero se importa moduloFuncionesGraficasBack, que tiene el root.mainloop() : 
import moduloFuncionesGraficasBack

# Ejecutar el loop principal de Tkinter
moduloFuncionesGraficasBack.root.mainloop()

#Primero se importa moduloFuncionesGraficasBack, que tiene el root.mainloop() : 
import moduloFuncionesGraficasBack