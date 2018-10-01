# resources/urls.py
from django.conf.urls import url
from . import views

app_name = 'resources'

urlpatterns = [
    # /
    url(r'^index/$', views.IndexView.as_view(), name='index'),

    # estudiante/<estudiante_id>  --> En la URL se encuentra como: estudiante/1 , donde el 1 seria el ID del estudiante.
    url(r'^estudiante/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detalles'),
    # Por razones de prueba estoy validando solo ID numericos.

    # /resources/estudiante/add/
    url(r'estudiante/add/$', views.CrearEstudiante.as_view(), name='estudiante-add'),

    # /resources/estudiante/2/
    url(r'estudiante/(?P<pk>[0-9]+)/$', views.UpdateEstudiante.as_view(), name='estudiante-update'),

    # /resources/estudiante/2/delete
    url(r'estudiante/(?P<pk>[0-9]+)/delete/$', views.DeleteEstudiante.as_view(), name='estudiante-delete'),
]
