import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'munoz_matias_FINAL.settings')
django.setup()

from app_seminario.models import Institucion, Inscrito
from datetime import datetime

# Crear datos para Instituciones
instituciones = [
    {'nombre': 'Instituto Gastronómico de Chile'},
    {'nombre': 'Academia de Cocina Internacional'},
    {'nombre': 'Centro de Innovación Gastronómica'},
]



# Crear datos para Inscritos
inscritos = [
    {
        'nombre': 'Juan Pérez',
        'correo': 'juan.perez@example.com',
        'nro_personas': 5,
        'telefono': '123456789',
        'fecha_inscripcion': datetime.now(),
        'institucion': Institucion.objects.first(),
        'estado': 'RESERVADO',
        'observacion': 'Asistirá con su equipo de trabajo.',
    },
    {
        'nombre': 'María López',
        'correo': 'maria.lopez@example.com',
        'nro_personas': 2,
        'telefono': '987654321',
        'fecha_inscripcion': datetime.now(),
        'institucion': Institucion.objects.last(),
        'estado': 'COMPLETADA',
    },
]

for inscrito_data in inscritos:
    inscrito, created = Inscrito.objects.get_or_create(**inscrito_data)
    


