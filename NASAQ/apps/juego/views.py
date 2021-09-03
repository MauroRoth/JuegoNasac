from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.categorias.models import Categoria
from apps.pregresp.models import PregYResp
from .models import Partida

# Create your views here.

@login_required
def Jugar(request, pk):
	context = {}
	objeto = Categoria.objects.get(id = pk)
	
	p = Partida.objects.create(usuario=request.user, categoria=objeto)
	g= PregYResp.objects.filter(categoria = objeto)[0]
	context['preguntas'] = g
	context['juego'] = p
	return render(request,'juego/preguntas.html',context)

@login_required
def Responder(request, pk):
	context = {}
	objeto = Partida.objects.get(id = pk)
	pregunta = PregYResp.objects.get(id = request.POST.get("id_pregunta"))

	respuesta = None
	for i in request.POST:
		if i != 'csrfmiddlewaretoken' and i != 'id_pregunta':
			respuesta=i 

	if respuesta==pregunta.respuesta_correcta:
		mensaje="Respuesta correcta! Adelante!!!"
		objeto.puntaje+=10
	else:
		mensaje="Respuesta incorrecta! Siga participando!!!"
	
	context['mensaje']=mensaje

	objeto.pregunta_actual+=1
	objeto.save()
	context['juego']=objeto
	return render(request,'juego/resultado.html',context)

@login_required
def Siguiente(request, pk):
	context = {}
	objeto = Partida.objects.get(id = pk)
	actual=objeto.pregunta_actual
	if actual < 7:
		g= PregYResp.objects.filter(categoria = objeto.categoria)[actual]
		context['preguntas'] = g
		context['juego'] = objeto
	else:
		context['juego']=objeto
		return render(request, 'juego/final.html',context)

	return render(request,'juego/preguntas.html',context)

@login_required
def Ranking(request):
	context={}
	ranking = Partida.objects.all().order_by('-puntaje')[:10]

	context['ranking']=ranking
	return render(request, 'juego/ranking.html',context)


