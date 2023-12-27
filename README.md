# sibiendo flask a Vercel
Creación del entorno virtual:
$ python -m venv ev-flask
Activación del entorno virtual (Windows) ejecutando:
$ ev-flask\Scripts\activate
Actualización del instalador de paquetes de python:
$ (ev-flask) python -m pip install --upgrade pip
Instalación de Flask utilizando pip:
$ (ev-flask) pip install flask flask-login flask-mysqldb flask-wtf email-validator
Verificar los paquetes instalados en el entorno virtual:
$ (ev-flask) pip freeze
