import datetime

from django.db import models


# Create your models here.
class Tarea(models.Model):
    tarea = models.CharField(max_length=140)
    dia = models.DateField(default=datetime.date.today)
    hora = models.TimeField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.tarea[:30], self.dia, self.hora)
