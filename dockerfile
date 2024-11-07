FROM python:3.11
#Esto indica la distro / especializacion que va a usar docker.

COPY . /app
#Esto copia lo que queremos al working directory (2 parámetros).

WORKDIR /app
#Esto indica el working directory.

RUN pip install -r requirements.txt
#Esto instala las dependencias.

CMD ["python","app.py"]
#Esto especifica lo que se va a correr siempre que empiece el container.

ENV LC_ALL C
#Esto le dice a Docker que solo use el formato estándar.