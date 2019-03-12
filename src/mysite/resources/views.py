from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante

from django.contrib.auth.models import User
from .forms import RegistroForm, ProfesorForm

# Librerias para Servicio de Rest:

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from .models import Evaluacion
from .serializers import EstudianteSerializer
from .serializers import EvaluacionSerializer
# from .models import EvaluacionForm


#///////////////////////// (** LOGN PROCESS VIEWS **) //////////////////////////////////////

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'resources/index.html')
@login_required
def special(request):
    return HttpResponse("Has iniciado sesión!")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegistroForm(data=request.POST)
        profesor_form = ProfesorForm(data=request.POST)
        if user_form.is_valid() and profesor_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profesor = profesor_form.save(commit=False)  #profesor se usa para mostrar los datos del perfil del profesor.
            profesor.user = user
            profesor.save()
            registered = True
        else:
            print(user_form.errors,profesor_form.errors)
    else:
        user_form = RegistroForm()
        profesor_form = ProfesorForm()
    return render(request,'resources/registrar.html',
                          {'user_form':user_form,
                           'profesor_form':profesor_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Tu cuenta fue desactivada.")
        else:
            print("Alguien intentó iniciar sesión y falló.")
            print("Uso el nombre de usuario: {} y la contraseña: {}".format(username,password))
            return HttpResponse("Datos de inicio de sesión no válidos dados")
    else:
        return render(request, 'resources/login_form.html', {})

#///////////////////////////////////////////////////////////////////////////////////////////


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


class RegistroUsuario(CreateView):
    model = User
    template_name = "resources/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')


# Vista para Realizar Evaluaciones del Modelo "Evaluacion"
class RealizarEvaluacionVista(CreateView):
    model = Evaluacion
    template_name = "resources/evaluacion_form.html"

    success_url = "/estudiante/{estudiante_id}"  # Esto es para direcionar hacia los detalles del estudiante
    # luego de registrar la evaluacion que se le ha realizo.
    fields = ['estudiante', 'es_favorito', 'evaluacion_tipo', 'fluidez_lectora', 'tipo_lectura', 'comentario',
              'texto_a_leer']

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context.update({
            'all_estudiantes': Estudiante.objects.all(),
        })
        return context

    def get_queryset(self):
        return Estudiante.objects.all()


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
