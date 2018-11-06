from django.db import models
from django.core.urlresolvers import reverse


# Crea tus Modelos aqui.



class Estudiante(models.Model):
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    genero = models.CharField(max_length=10)
    edad = models.CharField(max_length=8)
    foto = models.FileField()
    es_favorito = models.BooleanField(default=False)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('resources:detalles', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombres + ' - ' + self.apellidos


class Evaluacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    evaluacion_id = models.CharField(max_length=5)
    evaluacion_tipo = models.CharField(max_length=15)  # Los tipos de evaluacion son de Comprension o Fluidez Lectora.
    es_favorito = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('resources:favorito', kwargs={'pk': self.pk})

    def __str__(self):
        return self.evaluacion_id + ' - ' + self.evaluacion_tipo


class Fluidez(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    ppm = models.CharField(max_length=8)
    tipo_lectura = models.CharField(max_length=250)  # Tipos: LENTA, MUY LENTA, RAPIDA, etc.S


class Comprension(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    comprension_porcentaje = models.CharField(max_length=4)


#Realizar Evaluaciones:
class EvaluacionForm(models.Model):
    texto_a_leer = models.CharField(max_length=500, default='María conoce un niño con muy mal carácter en su escuela')
    #resultado = JSONField(max_length=200, default='')
    #Este ultimo campo es la respuesta luego de evaluar la lectura --> campo imprime resultado en un json.

    #resultado = models.JSONField(max_length=200)


