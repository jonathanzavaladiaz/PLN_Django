Instalar Django _pip instal django_

Crear un nuevo proyecto:
_django-admin startproyect -nombre-_

Arracnar en el servidor:
_python manage.py runserver_

Crear una aplicacion
python manage.py startapp interfaz

En el archivo configuracion, poner en la parte _APP_ la aplicacion creada

**CREAR SECCION NOSOTROS**
Primero debemos crear lo siguiente:
-Carpeta llamada template
-Dentro de la carpeta template creamos otra que se llame paginas. Estas van a contener todos los documentos HTML, y creamos uno.
_Para ver esos archivos HTML_

Debemos modificar dos archivos:
-views.py
-urls.py

En la parte de urls, solamente es poner el Path
En la parte de views es poner el siguinte codigo:
{def agente(request):
return render(request, "paginas/agente.html")}
