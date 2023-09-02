import datetime

from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=140)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.task[:30], self.date, self.time)
