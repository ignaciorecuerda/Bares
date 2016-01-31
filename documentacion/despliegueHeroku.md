[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://apozo-bc.herokuapp.com/Bares/)

Para desplegar nuestra app en Heroku, una vez clonado el repositorio de esta, tecleamos en el terminal:
```
heroku create apozo-bc
git push heroku master
```
Con heroku create, si no le indicamos nada, nos crea la app con un nombre aleatorio, en mi caso le he especificado un nombre, que ha sido [apozo-bc](apozo-bc.herokuapp.com/Bares/).
Para que funcione la aplicación con el modo ```DEBUG = false```, es decir, en explotación se han hecho las siguientes modificaciones:

- Archivo [settings.py](https://github.com/AntonioPozo/Bares/blob/master/proyectoP4/settings.py):

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
- Archivo [urls.py](https://github.com/AntonioPozo/Bares/blob/master/proyectoP4/urls.py):


```
Debug = False
ALLOWED_HOSTS = ['*']

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
```
**Nota:** Para un funcionamiento óptimo de la aplicación, el contenido estático de la misma no debería ser servido por Django, sino por el propio servidor. Sin embargo, la pérdida de rendimiento en este momento la considero irrelevante. 

Puede ver la aplicación funcionando [aquí](hhtp://www.apozo-bc.herokuapp.com/Bares/).
