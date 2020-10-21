from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from deliveries.models import Delivery
from deliveries.serializers import DeliverySerializer
from rest_framework.decorators import api_view

import json
from dijkstra import Graph, DijkstraSPF

@api_view(['GET', 'POST'])
def delivery_list(request):
    if request.method == 'GET':
        deliveries = Delivery.objects.all()
        
        map_name = request.query_params.get('map_name', None)
        if map_name is not None:
            deliveries = deliveries.filter(map_name__icontains=map_name)
        
        deliveries_serializer = DeliverySerializer(deliveries, many=True)
        return JsonResponse(deliveries_serializer.data, safe=False)
 
    elif request.method == 'POST':
        delivery_data = JSONParser().parse(request)
        delivery_serializer = DeliverySerializer(data=delivery_data)
        if delivery_serializer.is_valid():
            delivery_serializer.save()
            return JsonResponse(delivery_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(delivery_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delivery_process(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        map_name = body['map_name']
        origin = body['origin']
        destination = body['destination']
        truck_range = body['truck_range']
        fuel_cost = body['fuel_cost']

        if map_name == "" or map_name == "[]" or map_name is None:
            return JsonResponse("Invalid Parameters", status=status.HTTP_400_BAD_REQUEST, safe=False)

        deliveries = Delivery.objects.all()
        deliveries = deliveries.filter(map_name__icontains=map_name)
        if deliveries.count() == 0:
            return JsonResponse("Invalid Parameters: map name not found", status=status.HTTP_400_BAD_REQUEST, safe=False)
        
        deliveries_serializer = DeliverySerializer(deliveries, many=True)
        deliveries = dict(deliveries_serializer.data[0])['routes']

        nodes = set([origin, destination])
        g = Graph()
        for delivery in deliveries:
            route = list(delivery.items())
            nodes.add(route[0][1])
            nodes.add(route[1][1])
            g.add_edge(route[0][1], route[1][1], route[2][1])

        dijkstra = DijkstraSPF(g, origin)
        
        shortest_distance = dijkstra.get_distance(destination)
        path = " -> ".join(dijkstra.get_path(destination))
        cost = (shortest_distance / truck_range) * fuel_cost
        return JsonResponse({"route": path, "cost": cost}, safe=False)