from django.urls import path, include
from .import views


app_name = 'juego'

urlpatterns = [
	path('jugar/<int:pk>', views.Jugar, name = 'jugar'),
	path('respuesta/<int:pk>', views.Responder, name = 'respuesta'),
	path('siguiente/<int:pk>', views.Siguiente, name = 'siguiente'),
	path('ranking/', views.Ranking, name = 'ranking'),

]


