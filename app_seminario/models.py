from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    nombre_participante = models.CharField(max_length=100)
    email = models.EmailField()
    nro_personas = models.IntegerField()
    telefono = models.CharField(max_length=15)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=[('RESERVADO', 'Reservado'), ('CONFIRMADO', 'Confirmado')])
    observacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre_participante

