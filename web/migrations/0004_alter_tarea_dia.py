# Generated by Django 3.2.3 on 2021-05-24 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_tarea_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='dia',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
