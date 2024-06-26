from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lineas_accion/', views.lineas_accion, name='lineas_accion'),
    path('lineas_accion_1/', views.la1, name='lineas_accion_1'),
    path('lineas_accion_2/', views.graficos_l2, name='lineas_accion_2'),
    path('lineas_accion_3/', views.graficos_l3, name='lineas_accion_3'),
    path('lineas_accion_4/', views.graficos_l4, name='lineas_accion_4'),
    path('repositorio/', views.repositorio, name='repositorio'),
    # path('test/', views.grafico_41, name='test'),
]
