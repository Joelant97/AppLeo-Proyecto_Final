from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante, Profesor

#from django.contrib.auth.models import User
from .forms import RegistroForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

# Librerias para Servicio de Rest:

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from .models import Evaluacion
from .serializers import EstudianteSerializer
from .serializers import EvaluacionSerializer
# from .models import EvaluacionForm
from django.shortcuts import render
from rest_framework.response import Response
from .fusioncharts import FusionCharts





class RegistrarView(CreateView):
    model = Profesor
    form_class = RegistroForm
    template_name = "resources/registrar.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él
        y usamos authenticate para que el usuario incie sesión luego de haberse registrado
        y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

    # def form_valid(self, form):
    #     # Add logged-in user as autor of comment THIS IS THE KEY TO THE SOLUTION
    #     form.instance.profesor = self.request.user
    #
    #     # Call super-class form validation behaviour
    #     return super(RegistrarView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context.update({
            'all_profesors': Profesor.objects.all(),
        })
        return context

    def get_queryset(self):
        return Profesor.objects.all()

# class RegistroUsuario(CreateView):
#     model = User
#     template_name = "resources/registrar.html"
#     form_class = RegistroForm
#     success_url = reverse_lazy('login')
class ListProfesorLogeado(generic.ListView):
    template_name = 'resources/profesor-detalles.html'
    context_object_name = 'user.is_authenticated'
    slug_field = 'profesor'
    slug_url_kwarg = 'profesor'

    def get_queryset(self):
        return Profesor.objects.all()



class DetailViewProfesor(generic.DetailView):
    model = Profesor
    template_name = 'resources/profesor-detalles.html'
    # success_url = reverse_lazy('profesor-update')

'''
Vista para la Lectura, la cual solo sera vista por el estudiante: 

'''


# Crea tus Vistas aqui

def busqueda(request):
    estudiantes = Estudiante.objects.filter(nombres__icontains=request.GET['nombres']).values('id', 'nombres',
                                                                                              'apellidos')

    try:
        if estudiantes:
            return render_to_response('resources/buscar-resultados.html', {'estudiante': estudiantes})
    except:
        return HttpResponse("Hubo una excepcion")
    else:
        return HttpResponse("No hay estudiantes con ese nombre")





# Vista para Realizar Evaluaciones del Modelo "Evaluacion"
class RealizarEvaluacionVista(CreateView):
    model = Evaluacion
    template_name = "resources/evaluacion_form.html"

    success_url = "/estudiante/{estudiante_id}"  # Esto es para direcionar hacia los detalles del estudiante
    # luego de registrar la evaluacion que se le ha realizo.
    fields = ['estudiante', 'es_favorito', 'evaluacion_tipo', 'fluidez_lectora', 'tipo_lectura', 'comentario',
              'texto_a_leer']

    # def get_context_data(self, **kwargs):
    #     context = super(CreateView, self).get_context_data(**kwargs)
    #     context.update({
    #         'all_estudiantes': Estudiante.objects.all(),
    #     })
    #     return context
    #
    # def get_queryset(self):
    #     return Estudiante.objects.all()


# Eliminar las Evaluaciones:
def DeleteEvaluacion(request, eva_id):
    # El id de la Evaluacion a eliminar es id== eva_id

    eva_obj = get_object_or_404(Evaluacion, id=eva_id)
    eva_obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Esto te permite redirecionar a la misma pagina
    # en que estabas, luego de eliminar y actualizar.


class IndexView(generic.ListView):
    template_name = 'resources/index.html'
    context_object_name = 'all_estudiantes'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'all_evaluaciones': Evaluacion.objects.all(),
        })
        return context

    def get_queryset(self):
        return Estudiante.objects.all()


class DetailViewEvaluacion(generic.DetailView):
    model = Evaluacion
    template_name = 'resources/evaluacion-detalles.html'
    # success_url = reverse_lazy('estudiante-update')


class ListEstudiantes(generic.ListView):
    template_name = 'resources/estudiantes.html'
    context_object_name = 'all_estudiantes'
    slug_field = 'estudiante'
    slug_url_kwarg = 'estudiante'

    def get_queryset(self):
        return Estudiante.objects.all()


class DetailView(generic.DetailView):
    model = Estudiante
    template_name = 'resources/detalles.html'


class CrearEstudiante(CreateView):
    model = Estudiante
    fields = ['id', 'nombres', 'apellidos', 'genero', 'edad', 'foto']

    # success_url = "/estudiante/{estudiante_id}"
    # success_url = reverse_lazy('listado-estudiantes')

    def form_valid(self, form):
        # Add logged-in user as autor of comment THIS IS THE KEY TO THE SOLUTION
        form.instance.profesor = self.request.user

        # Call super-class form validation behaviour
        return super(CrearEstudiante, self).form_valid(form)


class UpdateEstudiante(UpdateView):
    model = Estudiante
    fields = ['id', 'nombres', 'apellidos', 'genero', 'edad', 'foto']


class DeleteEstudiante(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('resources:index')


''' 
    Vistas para las Graficas (Libreria: FusionCharts)
'''


def chart(request):
    dataSource= {}
    dataSource['chart'] = {
        "caption": "Velocidad de la lectura,",
        "subCaption": "evaluada segun su tipo",
        "xAxisName": "Tipo Lectura",
        "yAxisName": "Velocidad Lectora (En PPM)",
        "numberPrefix": "ppm",
        "theme": "zune"
    }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in Evaluacion.objects.all():
        data = {}
        data['label'] = key.tipo_lectura
        data['value'] = key.fluidez_lectora
        dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1", "600", "350", "chart-1", "json", dataSource)
    return render(request, 'resources/bar-chart.html', {'output': column2D.render()})


# Manejo de RestFull(Listar o crear uno nuevo del model para el Serv.Rest):
# /estudiantes
class EstudianteList(APIView):

    def get(self, request):
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# /evaluaciones
class EvaluacionList(APIView):  # Esto funciona como una especie de JSON.

    def get(self, request):
        evaluaciones = Evaluacion.objects.all()
        serializer = EvaluacionSerializer(evaluaciones, many=True)
        return Response(serializer.data)

    def post(self):
        pass
