from rest_framework import serializers

from backend.core.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'



