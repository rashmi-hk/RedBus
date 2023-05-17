
from rest_framework import serializers
from .models import Bus


class BusSerializer(serializers.ModelSerializer):
    """
    Client model serializer
    """

    class Meta:
        model = Bus
        fields = "__all__"