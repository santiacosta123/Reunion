from django.db import models

# Create your models here.
tipo_sexo = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('Otro', 'Otro'),
)


time_slots = (
    ('7:30 - 8:30', '7:30 - 8:30'),
    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


class Lider(models.Model):
    nombre_completo = models.CharField(primary_key=True, max_length= 50)
    # sexo = models.CharField(max_length=50, choices=tipo_sexo, default='Masculino')


    def __str__(self):
      return "%s" % (self.nombre_completo)


class Persona(models.Model):
    cedula = models.CharField(unique = True, max_length= 50)
    nombre_completo = models.CharField(primary_key=True, max_length= 50)
    telefono = models.CharField(max_length= 50)
    lider_referido = models.ForeignKey(Lider, on_delete=models.CASCADE)
    # sexo = models.CharField(max_length=50, choices=tipo_sexo, default='Masculino')

    def __str__(self):
    #   texto = "{0} ({1}) {2}"
    #   return texto.format(self.nombre_completo, self.cedula, self.telefono)
      return "%s" % (self.nombre_completo)




class Reunion(models.Model):
  descripcion_reunion = models.CharField(max_length=100, default='EVENTO 29 ENERO 2022')
#   fecha_evento = models.DateTimeField()
  fecha_evento = models.DateField()

  def __str__(self):
    return "%s %s" % (self.descripcion_reunion, self.fecha_evento)


class Asistencia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    reunion = models.CharField(max_length=100, default='EVENTO 29 ENERO 2022')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s %s" % (self.persona, self.reunion)


