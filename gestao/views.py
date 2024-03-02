from django.shortcuts import render, redirect
from .models import Casa, Registro
from .forms import CasaForm, RegistroForm, RegistroFormCasa, AtualizarRegistro
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View
from django.contrib import messages
from django.urls import reverse

# Create your views here.
# ---------- Views relacionadas à classe Casa ---------------

class NovaCasa(CreateView):
    model = Casa
    template_name = 'casa/cadastrar.html'
    form_class = CasaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Casa cadastrada com sucesso!")
        return reverse('home')
    
class Casas(ListView):
    model = Casa
    template_name='casa/listar.html'
    context_object_name = 'casas'

class ApagarCasa(DeleteView):
    model = Casa
    template_name = 'casa/apagar.html'       

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Casa apagada com sucesso!")
        return reverse('casas')

class AtualizarCasa(UpdateView):
    model = Casa
    template_name = 'casa/atualizar.html'
    form_class = CasaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Casa atualizada com sucesso!")
        return reverse('detalhar-casa', kwargs={'pk': self.object.pk})

class DetalharCasa(DetailView):
    model = Casa
    template_name = 'casa/detalhar.html'
    context_object_name = 'casa'

def NovoRegistroDaCasa(request, casa_id):
    casa = Casa.objects.get(pk=casa_id)
    if request.method == 'POST':
        form = RegistroFormCasa(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.casa = casa
            registro.save()
            return redirect('home')  # Redirecione para a página de sucesso após a criação do registro
    else:
        form = RegistroFormCasa(initial={'casa': casa})
    return render(request, 'casa/novo_registro.html', {'form': form})

# ---------- Views relacionadas à classe Registro ---------------
    
class NovoRegistro(CreateView):
    model = Registro
    template_name = 'registro/cadastrar.html'
    form_class = RegistroForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Registro cadastrado com sucesso!")
        return reverse('home')
    
class Registros(ListView):
    model = Registro
    template_name='registro/listar.html'
    context_object_name = 'registros'
    ordering = '-data'

class ApagarRegistro(DeleteView):
    model = Registro
    template_name = 'registro/apagar.html'       

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Registro apagado com sucesso!")
        return reverse('registros')

class AtualizarRegistro(UpdateView):
    model = Registro
    template_name = 'registro/atualizar.html'
    form_class = AtualizarRegistro

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Registro atualizado com sucesso!")
        return reverse('detalhar-registro', kwargs={'pk': self.object.pk})

class DetalharRegistro(DetailView):
    model = Registro
    template_name = 'registro/detalhar.html'
    context_object_name = 'registro'

# class RegistroDaCasa(View):
#     template_name = 'registro/historico.html'

#     def get_context_data(self, casaid, **kwargs):
#         casa = Casa.objects.filter(pk=casaid)
#         registro = Registro.objects.filter(casa=casa)          

#     return context


# def detalhar_registro(request, casa_id):
#     casa = Casa.objects.get(pk=casa_id)
#     registros = Registro.objects.filter(casa=casa).order_by('-data')
#     return render(request, 'registro/historico.html', {'casa': casa, 'registros': registros})