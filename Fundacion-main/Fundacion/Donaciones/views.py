from django.shortcuts import render, redirect
from .models import Donaciones
from .forms import DonacionForm
from django.http import HttpResponse, HttpResponseRedirect



# las clases genericas
from django.views.generic import ListView, CreateView
# esta libreria nos permitira redireccionamiento
from django.urls import reverse_lazy

#------------CLASES GENERICS-----------------------------------------------
# --Otra forma usando clases Generics -------
class DonacionCreate(CreateView):
    model = Donaciones
    form_class = DonacionForm
    template_name = 'Mandato/donacion.html'
    success_url = reverse_lazy("add_donacion")
    
class DonacionList(ListView):
    model = Donaciones
    template_name = 'Mandato/list_donacion.html'


# def donaciones(request):
#    if request.method == 'POST':
#       form = DonacionForm(request.POST)
#       if form.is_valid():
#           return HttpResponseRedirect('add_donacion')

#    else:
#       form = DonacionForm()

#    return render(request, 'Mandato/donacion.html', {'form': form})
