from django.db import models
from django.utils import timezone


# Create your models here.
class Tarea(models.Model):
    tarea = models.CharField(max_length=140)
    dia = models.DateField(default=timezone.now)
    hora = models.TimeField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.tarea[:30], self.dia, self.hora)
