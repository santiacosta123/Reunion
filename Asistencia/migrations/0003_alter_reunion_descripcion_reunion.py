# Generated by Django 4.0 on 2022-01-29 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0002_remove_persona_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reunion',
            name='descripcion_reunion',
            field=models.CharField(default='EVENTO 29 ENERO 2022', max_length=100),
        ),
    ]
