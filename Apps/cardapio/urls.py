from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('restaurante/<slug:slug>', v.detail_restaurant, name='detail_restaurant'),
    path('novo-restaurante/', v.create_restaurant, name='create_restaurant'),
]
