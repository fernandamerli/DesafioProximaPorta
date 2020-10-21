from rest_framework import serializers 
from deliveries.models import Delivery
from deliveries.models import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['origin', 'destination', 'distance']

class DeliverySerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    class Meta:
        model = Delivery
        fields = ['map_name', 'routes']

    def create(self, validated_data):
        routes_data = validated_data.pop('routes')
        delivery = Delivery.objects.create(**validated_data)
        
        for route_data in routes_data:
            Route.objects.create(delivery=delivery, **route_data)
        return delivery