# COMANDOS PYTHON
## _Consultar la versión de Python por defecto_
```
python -V
```
## _Crear entorno Conda_
```
conda create -n flask python==3.8
```
## _Activar el entorno virtual_
```
conda activate django
```
## _Desactivar el entorno virtual_
```
(django2) conda deactivate
```
## _Listar los paquetes instalados en el entorno virtual_
```
(django) pip list
```
## _Instalar Django en el entorno virtual_
```
(django) pip install django
```
## _Instalar DjangoRest_
```
(django) pip install djangorestframework
```
## _Instalar pylint (sintaxis)_
```
conda install pylint
```
## _Sintaxis extendida_
```
pip install pylint-django
```
## _Instalar unipath_
```
pip install unipath
```
## _Manipular imágenes_
```
pip install pillow
```
___
# COMANDOS DJANGO Y DJANGO REST
## _Crear un proyecto de Django_
```
(django) django-admin startproject proyecto
```
## _Levantar servidor django_
```
python manage.py runserver
```
## _Levantar servidor django con otra configuración de settings_
```
python manage.py runserver --settings=empleados.settings.local
```
## _Crear app_
```
django-admin startapp 'ruta/nombre de la app'
```
## _Fichero de migraciones_
```
python manage.py  makemigrations portfolio
```
## _Sincronizar la base de datos_
```
python manage.py migrate
```
## _Crear súper usuario administrador_
```
python manage.py createsuperuser
```
## _Crear copia de seguridad django_
```
python manage.py dumpdata > nombre_copia.json
```
## _Volcar información hacia el proyecto_
```
python manage.py loaddata nombre_copia.json
```
## _instalar editor_
```
pip install django-ckeditor
```
## _Instalar adaptador conexión base de datos postgres_
```
pip install psycopg2
```
## _instalar paquetes del proyecto_
```
pip install -r requirements/local.txt
```