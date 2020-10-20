from rest_framework import serializers 
from deliveries.models import Delivery
from deliveries.models import Route

# class DeliverySerializer(serializers.ModelSerializer):
#     routes = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all(), many=True)

#     class Meta:
#         model = Delivery
#         fields = ('id', 'map_name', 'routes')


# class RouteSerializer(serializers.ModelSerializer):
#     route_list = DeliverySerializer(many=True, read_only=True)

#     class Meta:
#         model = Route
#         fields = ('origin', 'destination', 'distance', 'route_list')

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
        file = open('debug.txt', 'w')
        
        for route_data in routes_data:
            file.write(str(route_data))
            Route.objects.create(delivery=delivery, **route_data)
        file.close()
        return delivery