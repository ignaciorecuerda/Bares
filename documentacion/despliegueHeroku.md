[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://apozo-bc.herokuapp.com/Bares/)

Para desplegar nuestra app en Heroku, una vez clonado el repositorio de esta, tecleamos en el terminal:
```
heroku create apozo-bc
git push heroku master
```
Con heroku create, si no le indicamos nada, nos crea la app con un nombre aleatorio, en mi caso le he especificado un nombre, que ha sido [apozo-bc](https:apozo-bc.herokuapp.com/Bares/).
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

<!--
Lo proximo que he hecho ha sido crear un proceso de integración contínua junto al despliegue automático tanto en Heroku como en Snap CI. Para realizarlo en heroku, al conectarlo con GitHub debes aceptar la siguiente ventana emergente:

![heroku123](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-11-16%20005315_zpssvdmjoei.png)

Una vez hecho esto, habilitamos que no despliegue hasta que no pase los tests para la IC:

![ic](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-11-16%20005451_zpsca57kxdz.png)

Como se puede ver en la imagen el proceso de intregración continua está correctamente configurado.
Otra opción es hacerlo con Snap CI, en el cual debes conectarte con GitHub y aceptar las condiciones:

![snap](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-11-16%20003846_zpspefwdnws.png)

Y por último, podemos comprobar que también está correctamente configurado el proceso de IC con Snap CI:

![snap1222](http://i1042.photobucket.com/albums/b422/Pedro_Gazquez_Navarrete/Captura%20de%20pantalla%20de%202015-11-16%20004423_zpsqfhzcdku.png)
-->