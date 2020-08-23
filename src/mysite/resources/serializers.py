# Esta clase maneja los JSON para hacer el servicio RestFull.


from rest_framework import serializers
from .models import Estudiante
from .models import Evaluacion

class EstudianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudiante
        fields = ('id', 'nombres')
        #fields = '__all__'     #Si quieres imprimir todos los campos (fields).


class EvaluacionSerializer(serializers.ModelSerializer):

    estudiante = EstudianteSerializer()
    class Meta:
        model = Evaluacion
        fields = ('id', 'fluidez_lectora', 'tipo_lectura', 'evaluacion_tipo', 'es_favorito', 'fecha', 'estudiante')
        # read_only_fields = ('type','timestamp')

    # fields = '__all__'

