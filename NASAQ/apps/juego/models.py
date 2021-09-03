from django.db import models
from apps.categorias.models import Categoria
from apps.usuarios.models import Usuario

# Create your models here.

class Partida(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	puntaje = models.IntegerField(default = 0)
	pregunta_actual = models.IntegerField(default = 0)
	
	
	
	


	