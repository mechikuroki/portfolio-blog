# Blog en Django

Password del db.sqlite3 default es admin usuario admin

## Seteo:
```
pip install django django-tailwind markdown

npm install

#Si se borra la base de datos modelo

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

#Si se quiere editar la parte gráfica se entra a la app theme, y se corre "npm install". Cuando se altera el CSS se corre:

npx @tailwindcss/cli -i ./static/input.css -o ./static/css/dist/styles.css --minify #o --watch si va a ser editado 
```

## Para correrlo en development (para lo que está preparado):

```

python manage.py runserver

```
