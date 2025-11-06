from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_clinicanutricional, name='inicio_clinicanutricional'),
    path('agregar_nutriologo/', views.agregar_nutriologo, name='agregar_nutriologo'),
    path('ver_nutriologos/', views.ver_nutriologos, name='ver_nutriologos'),
    path('actualizar_nutriologo/<int:id>/', views.actualizar_nutriologo, name='actualizar_nutriologo'),
    path('realizar_actualizacion_nutriologo/<int:id>/', views.realizar_actualizacion_nutriologo, name='realizar_actualizacion_nutriologo'),
    path('borrar_nutriologo/<int:id>/', views.borrar_nutriologo, name='borrar_nutriologo'),
]