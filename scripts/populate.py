from django.db import IntegrityError
from app_seminario.models import Institucion, Inscrito

def populate_instituciones():
    """Crea instituciones iniciales si no existen."""
    instituciones_iniciales = [
        "Instituto de Gastronomía Internacional",
        "Escuela de Cocina Moderna",
        "Universidad de Gastronomía y Turismo",
        "Centro Gastronómico Avanzado"
    ]

    for nombre in instituciones_iniciales:
        try:
            Institucion.objects.create(nombre=nombre)
            print(f"Institución creada: {nombre}")
        except IntegrityError:
            print(f"Institución ya existente: {nombre}")

def populate_inscritos():
    """Crea inscritos iniciales si no existen (ejemplo de relación con instituciones)."""
    if Institucion.objects.exists():
        instituto = Institucion.objects.first()  # Usar la primera institución creada como ejemplo.
        try:
            Inscrito.objects.create(
                nombre_participante="Juan Pérez",
                email="juan.perez@example.com",
                nro_personas=5,
                telefono="1234567890",
                institucion=instituto,
                estado="RESERVADO"
            )
            print("Inscrito creado: Juan Pérez")
        except IntegrityError:
            print("Inscrito ya existente: Juan Pérez")

def run():
    """Ejecuta las funciones de población."""
    print("Iniciando población de datos...")
    populate_instituciones()
    populate_inscritos()
    print("Población de datos completada.")
