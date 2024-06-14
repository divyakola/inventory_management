from django.urls import path
from .views import product_insert,display

urlpatterns=[
    path('insert',product_insert),
    path('show',display)
]