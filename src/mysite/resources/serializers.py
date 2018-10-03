# Esta clase maneja los JSON para hacer el servicio RestFull.


from rest_framework import serializers
from .models import Estudiante
from .models import Evaluacion

class EstudianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudiante
        fields = ('estudiante_id', 'nombres')
        #fields = '__all__'



class EvaluacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evaluacion
        fields = ('evaluacion_id', 'evaluacion_tipo')


