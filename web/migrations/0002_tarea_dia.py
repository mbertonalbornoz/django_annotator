# Generated by Django 3.2.3 on 2021-05-24 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='dia',
            field=models.DateField(default=datetime.datetime(2021, 5, 24, 18, 48, 52, 719254)),
        ),
    ]
