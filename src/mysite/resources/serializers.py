# Esta clase maneja los JSON para hacer el servicio RestFull.


from rest_framework import serializers
from .models import Estudiante
from .models import Evaluacion

class EstudianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudiante
        fields = ('id', 'nombres', 'es_favorito')
        #fields = '__all__'     #Si quieres imprimir todos los campos (fields).


class EvaluacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evaluacion
        fields = ('evaluacion_id', 'evaluacion_tipo', 'es_favorito')


