from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Estudiante


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
    fields = ['estudiante_id', 'estudiante_nombre', 'estudiante_apellido', 'estudiante_genero', 'nacimiento', 'edad', 'estudiante_logo']


