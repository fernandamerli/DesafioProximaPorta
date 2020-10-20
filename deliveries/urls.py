from django.conf.urls import url 
from deliveries import views 
 
urlpatterns = [ 
    url(r'^api/deliveries$', views.delivery_list)
]