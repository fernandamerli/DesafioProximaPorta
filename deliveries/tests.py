import json
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_get_delivery(client):
   url = reverse('delivery-list')
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_post_delivery(client):
   url = reverse('delivery-list')
   data = {
      "map_name": "mapa 1",
      "routes": [
        {
            "origin": "a",
            "destination": "b",
            "distance": 10
        }
    ]
   }
   response = client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == 201

@pytest.mark.django_db
@pytest.mark.parametrize(
   'map_name, origin, destination, truck_range, fuel_cost, status_code', [
        ('mapa 1', 'a', 'b', 10, 2.5, 200), #success
        ('', 'a', 'b', 10, 2.5, 400) #error
   ]
)
def test_process_delivery(map_name, origin, destination, truck_range, fuel_cost, status_code, client):
   url1 = reverse('delivery-list')
   url2 = reverse('delivery-process')
   data1 = {
      "map_name": "mapa 1",
      "routes": [
        {
            "origin": "a",
            "destination": "b",
            "distance": 10
        }
    ]
   }
   response = client.post(url1, content_type='application/json', data=json.dumps(data1))
   data2 = {
        'map_name': map_name,
        'origin': origin,
        'destination': destination,
        'truck_range': truck_range,
        'fuel_cost': fuel_cost
   }
   response = client.post(url2, content_type='application/json', data=json.dumps(data2))
   assert response.status_code == status_code