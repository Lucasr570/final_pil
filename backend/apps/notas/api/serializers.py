# Rest imports
from rest_framework import serializers

# Models imports
from apps.notas.models import Notas


# Serializers
class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = '__all__'
        


class NotasListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'user': instance['user'],
            'evento': instance['evento'],
            'fecha': instance['fecha']
        }