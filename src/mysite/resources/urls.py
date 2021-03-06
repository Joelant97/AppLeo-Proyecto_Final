# resources/urls.py
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

app_name = 'resources'

urlpatterns = [
    # /
    url(r'^index/$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^reportes/$', login_required(views.ReportesView.as_view()), name='reportes'),

    #lectura/estudiante/
    #url(r'lectura/estudiante/$', login_required(views.LecturaEstudianteView.as_view()), name='estudiante-lectura'),

    # profesor/perfil/<profesor_id>
    url(r'^profesor/perfil/$', login_required(views.ListProfesorLogeado.as_view()), name='profesor-perfil'),
    #url(r'^profesor/perfil/(?P<pk>[0-9]+)/$', login_required(views.ListProfesorLogeado.as_view()), name='profesor-perfil'),

    # estudiante/<estudiante_id>  --> En la URL se encuentra como: estudiante/1 , donde el 1 seria el ID del estudiante.
    url(r'^estudiante/(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detalles'),
    # Por razones de prueba estoy validando solo ID numericos.

    url(r'estudiante/buscar/$', login_required(views.busqueda), name='estudiante-buscar'),

    url(r'listado/estudiantes/$', login_required(views.ListEstudiantes.as_view()), name='listado-estudiantes'),

    # /resources/estudiante/add/
    url(r'estudiante/add/$', login_required(views.CrearEstudiante.as_view()), name='estudiante-add'),

    # /resources/lectura/add/
    url(r'lectura/add/$', login_required(views.CrearLectura.as_view()), name='lectura-add'),

    # /resources/listado/lecturas/
    url(r'listado/lecturas/$', login_required(views.ListLecturas.as_view()), name='listado-lecturas'),

    # /resources/lectura/update/2/
    url(r'lectura/update/(?P<pk>[0-9]+)/$', login_required(views.UpdateLectura.as_view()), name='lectura-update'),

    # /resources/lectura/2/delete
    url(r'lectura/(?P<pk>[0-9]+)/delete/$', login_required(views.DeleteLectura.as_view()), name='lectura-delete'),

    # /resources/estudiante/update/2/
    url(r'estudiante/update/(?P<pk>[0-9]+)/$', login_required(views.UpdateEstudiante.as_view()), name='estudiante-update'),

    # /resources/estudiante/2/delete
    url(r'estudiante/(?P<pk>[0-9]+)/delete/$', login_required(views.DeleteEstudiante.as_view()), name='estudiante-delete'),

    # evaluacion/<evaluacion_id>
    url(r'^evaluacion/(?P<pk>[0-9]+)/$', login_required(views.DetailViewEvaluacion.as_view()), name='detalles-evaluacion'),

    # /evaluacion/
    url(r'evaluacion/add/$', login_required(views.RealizarEvaluacionVista.as_view()), name='realizar-evaluacion'),

    # /resources/estudiante/2/delete
    url(r'evaluacion/delete/(?P<eva_id>[\d]+)/$', login_required(views.DeleteEvaluacion), name='evaluacion-delete'),

    # api/chart/data/ --> Ruta para generar la grafica.
    url(r'appleo/api/chart/data/', login_required(views.chart)),

    url(r'logout/', logout_then_login, name='logout'),



]

