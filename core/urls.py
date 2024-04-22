from django.urls import path
from . import views

urlpatterns = [
    path('', views.plot, name='plot'),
    path('lineas_accion/', views.lineas_accion, name='lineas_accion'),
    path('lineas_accion_1/', views.plot2, name='lineas_accion_1')
]
