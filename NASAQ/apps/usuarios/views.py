from django.shortcuts import render
from .forms import RegistroFormulario


# Create your views here.

def Registro(response):
	if response.method == 'POST':
		form = RegistroFormulario (response.POST)
		if form.is_valid():
			form.save()

	else:
		form = RegistroFormulario()

	return render(response, 'usuarios/registro.html', {'form' : form})


