from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_customer', views.createCustomer, name='createCustomer'),
    path('get_customer', views.get_customer, name='customers'),
    path('delete_customer', views.delete_customer, name='del_customers'),
    path('update_customer', views.update_customer, name='update_customers'),
]

# http://127.0.0.1:8000/            customer    /get_customer   ----> url
# Base url(Main Project folder)     app_name    endpoint