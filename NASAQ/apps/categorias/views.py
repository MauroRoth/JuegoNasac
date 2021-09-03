from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Categoria




# Create your views here.

@login_required
def ListarCategorias(request):
	context = {}
	# BUSCAR TODOS LOS CATEGORIAS DE LA BD
	#Categorias.objects.all() SE TRANFORMA EN:
	# SELECT * FROM Categorias
	todas = Categoria.objects.all() #ORM DE DJANGO
	# PASARLOS AL TEMPLATE

	context['categorias'] = todas # ESTO ES UNA LISTA DE OBJETOS
	
	return render(request,'juego/categoriaJuego.html',context)


