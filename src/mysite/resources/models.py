from django.db import models

# Crea tus Modelos aqui.

class Profesor(models.Model):
    profesor_nombre = models.CharField(max_length=250)
    profesor_apellido = models.CharField(max_length=250)
    profesor_email = models.EmailField(max_length=250)
    profesor_telefono = models.CharField(max_length=15)
    profesor_genero = models.CharField(max_length=10)
    institucion = models.CharField(max_length=250)



class Estudiante(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante_nombre = models.CharField(max_length=250)
    estudiante_apellido = models.CharField(max_length=250)
    estudiante_genero = models.CharField(max_length=10)
    nacimiento = models.DateField(max_length=10)
    edad = models.CharField(max_length=8)


class Evaluacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    evaluacion_id = models.CharField(max_length=5)
    evaluacion_tipo = models.CharField(max_length=15)   #Los tipos de evaluacion son de Comprension o Fluidez Lectora.


class Fluidez(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    ppm = models.CharField(max_length=8)
    tipo_lectura = models.CharField(max_length=250)   #Tipos: LENTA, MUY LENTA, RAPIDA, etc.



class Comprension(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    comprension_porcentaje = models.CharField(max_length=4)


