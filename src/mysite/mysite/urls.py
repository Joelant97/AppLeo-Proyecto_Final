"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login

from rest_framework.urlpatterns import format_suffix_patterns
from resources.views import EstudianteList
from resources.views import EvaluacionList
from resources.views import RegistrarView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('resources.urls', namespace='resources')),
    url(r'^$', login, {'template_name': 'resources/login_form.html'}, name='user_login'),
    url(r'^accounts/user_login/$', login, {'template_name': 'resources/login_form.html'}, name='user_login'),
    url(r'^registrate/$', RegistrarView.as_view(), name='registrar'),
    #url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),

    #Password Reset URL's
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$', auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password_reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),

    #url(r'^', include('django.contrib.auth.urls')),


    #estudiantes y evaluaciones son listas de Rest (Servicio RESTful)
    url(r'^estudiantes/', login_required(EstudianteList.as_view()), name='estudiantes'),
    url(r'^evaluaciones/', login_required(EvaluacionList.as_view()), name='evaluaciones'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)