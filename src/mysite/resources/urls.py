# resources/urls.py
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

app_name = 'resources'

urlpatterns = [
    # /
    url(r'^index/$', login_required(views.IndexView.as_view()), name='index'),

    # estudiante/<estudiante_id>  --> En la URL se encuentra como: estudiante/1 , donde el 1 seria el ID del estudiante.
    url(r'^estudiante/(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detalles'),
    # Por razones de prueba estoy validando solo ID numericos.

    # /resources/estudiante/add/
    url(r'estudiante/add/$', login_required(views.CrearEstudiante.as_view()), name='estudiante-add'),

    # /resources/estudiante/2/
    url(r'estudiante/(?P<pk>[0-9]+)/$', login_required(views.UpdateEstudiante.as_view()), name='estudiante-update'),

    # /resources/estudiante/2/delete
    url(r'estudiante/(?P<pk>[0-9]+)/delete/$', login_required(views.DeleteEstudiante.as_view()), name='estudiante-delete'),

    url(r'logout/', logout_then_login, name='logout'),
]

