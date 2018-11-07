from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante

from django.contrib.auth.models import User
from .forms import RegistroForm

#Librerias para Servicio de Rest:
#from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework import status
from .models import Evaluacion
from .serializers import EstudianteSerializer
from .serializers import EvaluacionSerializer
from .models import EvaluacionForm


#Crea tus Vistas aqui

class RegistroUsuario(CreateView):
    model = User
    template_name = "resources/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')

class RegistroEvaluacion():
    model = Evaluacion
    template_name = "resources/evaluacion.html"
    success_url = reverse_lazy('resources:detalles')    #Esto es para direcionar hacia los detalles luego de registrar la
                                                        #evaluacion del estudiante.

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
    fields = ['id', 'nombres', 'apellidos', 'genero', 'edad', 'foto']


class UpdateEstudiante(UpdateView):
    model = Estudiante
    fields = ['id', 'nombres', 'apellidos', 'genero', 'edad', 'foto']


class DeleteEstudiante(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('resources:index')


#Manejo de RestFull(Listar o crear uno nuevo del model para el Serv.Rest):
#/estudiantes
class EstudianteList(APIView):

    def get(self, request):
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)

    def post(self):
        pass


#/evaluaciones
class EvaluacionList(APIView): #Esto funciona como una especie de JSON.

    def get(self, request):
        evaluaciones = Evaluacion.objects.all()
        serializer = EvaluacionSerializer(evaluaciones, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#Vista para Realizar Evaluaciones
class RealizarEvaluacionVista(CreateView):
    model = EvaluacionForm
    fields = ['texto_a_leer']


