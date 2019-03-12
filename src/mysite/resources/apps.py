from django.apps import AppConfig
from django.db.models.signals import post_migrate

# from .models import Profesor
#
# def do_stuff(sender, **kwargs):
#     Profesor.objects.get() # etc...

class ResourcesConfig(AppConfig):
    name = 'resources'

    # def ready(self):
    #     post_migrate.connect(do_stuff, sender=self)




