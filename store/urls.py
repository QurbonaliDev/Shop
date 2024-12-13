from django.urls import path

from store.views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/<slug>', products, name='products'),
    path('single/<int:pk>/', single, name='single'),
]
