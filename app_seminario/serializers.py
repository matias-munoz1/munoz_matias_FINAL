from rest_framework import serializers
from .models import Inscrito, Institucion

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ['id', 'nombre']

class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = [
            'id',
            'nombre_participante',
            'email',
            'nro_personas',
            'telefono',
            'institucion',
            'estado',
            'observacion',
        ]


class AutorSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    proyecto = serializers.CharField()
