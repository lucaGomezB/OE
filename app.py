from dotenv import load_dotenv
import os
load_dotenv()
#Acá se importa lo que usaremos

API_KEY = os.getenv('API_KEY')
#Con esto accedemos a la API

#Primero se importa moduloFuncionesGraficasBack, que tiene el root.mainloop() : 
import moduloFuncionesGraficasBack
<<<<<<< HEAD

=======
#Segundo, se importa moduloFuncionesBasicas, que deja correr el programa incluso cuando no se tiene cabeza.
import moduloFuncionesBasicas
>>>>>>> Development
# Ejecutar el loop principal de Tkinter

display_value = os.environ.get('DISPLAY')
if (display_value is None): 
<<<<<<< HEAD
    pass
=======
    moduloFuncionesBasicas.menu(0)
>>>>>>> Development
else:
    moduloFuncionesGraficasBack.root.mainloop()