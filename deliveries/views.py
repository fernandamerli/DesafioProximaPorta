from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from deliveries.models import Delivery
from deliveries.serializers import DeliverySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def delivery_list(request):
    if request.method == 'GET':
        deliveries = Delivery.objects.all()
        
        map_name = request.query_params.get('map_name', None)
        if map_name is not None:
            deliveries = deliveries.filter(map_name__icontains=map_name)
        
        deliveries_serializer = DeliverySerializer(deliveries, many=True)

        file = open('debug.txt', 'w')
        file.write(str(deliveries_serializer.data))
        file.close()

        return JsonResponse(deliveries_serializer.data, safe=False)
 
    elif request.method == 'POST':
        delivery_data = JSONParser().parse(request)
        delivery_serializer = DeliverySerializer(data=delivery_data)
        if delivery_serializer.is_valid():
            delivery_serializer.save()
            return JsonResponse(delivery_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(delivery_serializer.errors, status=status.HTTP_400_BAD_REQUEST)