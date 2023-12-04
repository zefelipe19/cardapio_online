from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('restaurante/<slug:slug>/', v.detail_restaurant, name='detail_restaurant'),
    path('restaurante/<slug:slug>/categorias/', v.detail_restaurant_category, name='detail_restaurant_category'),
    path('novo-restaurante/', v.create_restaurant, name='create_restaurant'),
    path('restaurante/<slug:slug>/adm', v.admin_area, name='admin_area'),
]
