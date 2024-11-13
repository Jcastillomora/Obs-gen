from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lineas_accion/', views.lineas_accion, name='lineas_accion'),
    path('repositorio/', views.repositorio, name='repositorio'),
    path('contacto/', views.contact_view, name='contacto'),
    # path('contact/', views.contact_view, name='contact'),
]
