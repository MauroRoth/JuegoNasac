from django.shortcuts import render


def Home(request):
	return render(request, 'home.html')

def Nosotros(request):
	return render(request, 'nosotros.html')

def Login(request):
	return render(request, 'usuarios/login.html')

def Registro(request):

	return render(request, 'usuarios/registro.html')

def Juego(request):
	return render(request, 'juego/nasac.html')

