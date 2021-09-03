from django.db import models
from apps.categorias.models import Categoria

# Create your models here.

class PregYResp(models.Model):
	pregunta = models.CharField(max_length = 200)
	respuesta1 = models.CharField(max_length = 200)
	respuesta2 = models.CharField(max_length = 200)
	respuesta3 = models.CharField(max_length = 200)
	respuesta_correcta = models.CharField(max_length=200)
	puntaje = models.IntegerField(default = 0)
	categoria = models.ForeignKey(Categoria, related_name= 'mi_categoria', on_delete = models.CASCADE , null = True)


	def __str__(self):
		return self.pregunta

	def getPuntaje(self):
		return self.puntaje







