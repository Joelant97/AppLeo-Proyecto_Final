from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from phone_field import PhoneField
from datetime import datetime

#from django.dispatch import receiver
#from django.db.models.signals import post_save
#from phonenumber_field.modelfields import PhoneNumberField

# Crea tus Modelos aqui.



class Profesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=250, blank=True)
    telefono = PhoneField(blank=True, help_text='Teléfono de contacto')

    #def from_db_value(self, usuario, direccion, telefono):

    # def __init__(self, usuario, direccion, telefono):
    #     # Input parameters are lists of cards ('Ah', '9s', etc.)
    #     self.usarioario = usuario
    #     self.direccion = direccion
    #     self.telefono = telefono

    def get_absolute_url(self):
        return reverse('resources:profesor-perfil', kwargs={'pk': self.pk})

    def __str__(self):
        return self.usuario.username

# @receiver(post_save, sender=User)
# def crear_usuario_profesor(sender, instance, created, **kwargs):
#     if created:
#         Profesor.objects.create(usuario=instance)
#
#
# @receiver(post_save, sender=User)
# def guardar_usuario_profesor(sender, instance, **kwargs):
#     instance.profesor.save()

#Modelo de los Grupos:
#class Grupo(models.Model):


class Estudiante(models.Model):
    #profesor =models.OneToOneField(Profesor, on_delete=models.CASCADE)  #Es mejor usar OneToOneField y eliminar el (unique = True).
    #profesor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    genero = models.CharField(max_length=10)
    edad = models.CharField(max_length=8)
    foto = models.FileField()
    #es_favorito = models.BooleanField(default=False)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('resources:detalles', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombres + ' - ' + self.apellidos

class Lectura(models.Model):
    titulo = models.CharField(max_length=250)
    texto = models.CharField(max_length=1500)


#Realizar Evaluaciones:
class Evaluacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    texto_a_leer = models.CharField(max_length=500, default='María conoce un niño con muy mal carácter en su escuela llamado Juan Carlos')
    evaluacion_tipo = models.CharField(max_length=15)  # Los tipos de evaluacion son de Comprension o Fluidez Lectora.
    fluidez_lectora = models.CharField(max_length=25, default='')
    tipo_lectura = models.CharField(max_length=250, default='')  # Tipos: LENTA, MUY LENTA, RAPIDA, etc.S
    es_favorito = models.BooleanField(default=False)
    comentario = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(default=datetime.now, blank=False)
    lectura = models.ForeignKey(Lectura, on_delete=models.CASCADE, blank=True, default='')

    #Los datos a imprimir en la graficas:
    def __unicode__(self):
        return u'%s %s %s' % (self.fluidez_lectora, self.tipo_lectura, self.fecha)

    def get_absolute_url(self):
        return reverse('resources:detalles-evaluacion', kwargs={'pk': self.pk})

    def __str__(self):
        return self.fluidez_lectora + ' - ' + self.tipo_lectura + ' - ' + self.fecha





#Las preguntas se usan para implementar Cloze.

class Pregunta(models.Model):
    lectura = models.ForeignKey(Lectura, on_delete=models.CASCADE, blank=True, default='')
    nombre_p1 = models.CharField(max_length=150, blank=True)
    enunciado_p1 = models.CharField(max_length=512, blank=True)
    nombre_p2 = models.CharField(max_length=150, blank=True)
    enunciado_p2 = models.CharField(max_length=512, blank=True)
    nombre_p3 = models.CharField(max_length=150, blank=True)
    enunciado_p3 = models.CharField(max_length=512, blank=True)
    nombre_p4 = models.CharField(max_length=150, blank=True)
    enunciado_p4 = models.CharField(max_length=512, blank=True)
    nombre_p5 = models.CharField(max_length=150, blank=True)
    enunciado_p5 = models.CharField(max_length=512, blank=True)



class Fluidez(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    ppm = models.CharField(max_length=8)
    tipo_lectura = models.CharField(max_length=250)


class Comprension(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    comprension_porcentaje = models.CharField(max_length=4)


#Realizar Evaluaciones:
#class EvaluacionForm(models.Model):
    #texto_a_leer = models.CharField(max_length=500, default='María conoce un niño con muy mal carácter en su escuela')


    #resultado = JSONField(max_length=200, default='')
    #Este ultimo campo es la respuesta luego de evaluar la lectura --> campo imprime resultado en un json.

    #resultado = models.JSONField(max_length=200)


