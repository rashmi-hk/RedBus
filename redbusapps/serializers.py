
from rest_framework import serializers
from .models import Bus,Restaurant


class BusSerializer(serializers.ModelSerializer):
    """
    Client model serializer
    """

    class Meta:
        model = Bus
        fields = "__all__"

class RestaurantSerializer(serializers.ModelSerializer):
    """
    Client model serializer
    """

    class Meta:
        model = Restaurant
        fields = "__all__"