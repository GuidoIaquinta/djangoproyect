from django.urls import path
from . import views

urlpatterns = [
    path('crear/<dni>/<nombre>/<apellido>/', views.crear),
    path('mostrar/', views.mostrar),
]
#esto es un ejemplo
