from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

ESTADOS = [
    ('RESERVADO', 'RESERVADO'),
    ('COMPLETADA', 'COMPLETADA'),
    ('ANULADA', 'ANULADA'),
    ('NO ASISTEN', 'NO ASISTEN'),
]

class Institucion(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nombre


class Inscrito(models.Model):
    nombre_participante = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    nro_personas = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    telefono = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_participante} - {self.institucion.nombre}"
