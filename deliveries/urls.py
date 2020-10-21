from django.conf.urls import url 
from deliveries import views 
 
urlpatterns = [ 
    url(r'^api/deliveries$', views.delivery_list),
    url(r'^api/deliveries/best_route$', views.delivery_process)
]