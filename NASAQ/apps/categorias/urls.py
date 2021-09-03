from django.urls import path, include
from .import views


app_name = 'categorias'

urlpatterns = [
	path('categorias/', views.ListarCategorias, name = 'categorias'),
	
]




