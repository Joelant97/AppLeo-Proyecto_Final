from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante

from django.contrib.auth.models import User
from .forms import RegistroForm


#Crea tus Vistas aqui

class RegistroUsuario(CreateView):
    model = User
    template_name = "resources/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')


class IndexView(generic.ListView):
    template_name = 'resources/index.html'
    context_object_name = 'all_estudiantes'

    def get_queryset(self):
        return Estudiante.objects.all()


class DetailView(generic.DetailView):
    model = Estudiante
    template_name = 'resources/detalles.html'


class CrearEstudiante(CreateView):
    model = Estudiante
    fields = ['estudiante_id', 'nombres', 'apellidos', 'genero', 'edad', 'foto']


class UpdateEstudiante(UpdateView):
    model = Estudiante
    fields = ['estudiante_id', 'nombres', 'apellidos', 'genero', 'edad', 'foto']


class DeleteEstudiante(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('resources:index')
