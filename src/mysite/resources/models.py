from django.db import models
from django.core.urlresolvers import reverse

# Crea tus Modelos aqui.

class Profesor(models.Model):
    profesor_id = models.CharField(max_length=5, default='Introduzca el ID')
    profesor_nombre = models.CharField(max_length=250)
    profesor_apellido = models.CharField(max_length=250)
    profesor_email = models.EmailField(max_length=250)
    profesor_telefono = models.CharField(max_length=15)
    profesor_genero = models.CharField(max_length=10)
    institucion = models.CharField(max_length=250)



class Estudiante(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante_id = models.CharField(max_length=5, default='Introduzca el ID')
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    genero = models.CharField(max_length=10)
    edad = models.CharField(max_length=8)
    foto = models.CharField(max_length=1000, default='LINK de la FOTO')

    def get_absolute_url(self):
        return reverse('resources:detalles', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombres + ' - ' + self.apellidos


class Evaluacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    evaluacion_id = models.CharField(max_length=5)
    evaluacion_tipo = models.CharField(max_length=15)   #Los tipos de evaluacion son de Comprension o Fluidez Lectora.
    es_favorito = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('resources:favorito', kwargs={'pk': self.pk})

    def __str__(self):
        return self.evaluacion_id + ' - ' + self.evaluacion_tipo

class Fluidez(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    ppm = models.CharField(max_length=8)
    tipo_lectura = models.CharField(max_length=250)   #Tipos: LENTA, MUY LENTA, RAPIDA, etc.



class Comprension(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    comprension_porcentaje = models.CharField(max_length=4)




