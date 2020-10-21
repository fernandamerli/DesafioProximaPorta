from django.conf.urls import url 
from deliveries import views 
 
urlpatterns = [ 
    url(r'^api/deliveries$', views.delivery_list, name='delivery-list'),
    url(r'^api/deliveries/best_route$', views.delivery_process, name='delivery-process')
]