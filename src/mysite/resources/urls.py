# resources/urls.py
from django.conf.urls import url
from . import views

app_name = 'resources'

urlpatterns = [
    # /evaluar/
    url(r'^$', views.index, name='index'),

    # /evaluar/<evaluacion_id>       --> 1 en este caso es el ID de la Evaluacion. (evaluacion_id).
    url(r'^(?P<evaluacion_id>[0-9]+)/$', views.detalles, name='detalles'),     #Por razones de prueba estoy validando los ID solo de 0-9.

]

