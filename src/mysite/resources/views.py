from django.views import generic
from .models import Estudiante


class IndexView(generic.ListView):
    template_name = 'resources/index.html'
    context_object_name = 'all_estudiantes'

    def get_queryset(self):
        return Estudiante.objects.all()




class DetailView(generic.DetailView):
    model = Estudiante
    template_name = 'resources/detalles.html'



