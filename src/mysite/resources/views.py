from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante


from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render

from .forms import UserLoginForm

#Crea tus Vistas aqui

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        usuario = form.cleaned_data.get("usuario")
        contraseña = form.cleaned_data.get('contraseña')

    return render(request, 'resources/form.html', {"form": form, "title": title})

def registro_view(request):
    return render(request, 'form.html', {})

def logout_view(request):
    return render(request, 'form.html', {})


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
