from rest_framework import serializers
from .models import Inscrito, Institucion

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ['id', 'nombre']

class InscritoSerializer(serializers.ModelSerializer):
    institucion_nombre = serializers.CharField(source='institucion.nombre', read_only=True)
    class Meta:
        model = Inscrito
        fields = ['id', 'nombre_participante', 'email', 'nro_personas', 'telefono', 'fecha_inscripcion',
                  'hora_inscripcion', 'institucion', 'institucion_nombre', 'estado', 'observacion']

# Autor del proyecto (Datos Hardcodeados o proveniente de configuración)
class AutorSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    proyecto = serializers.CharField()
