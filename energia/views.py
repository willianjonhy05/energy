from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib import messages
from gestao.models import Casa, Registro
from gestao.forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.


# class HistoricoCasa(TemplateView):
#     template_name = 'registro/historico1.html'
#     registros_por_pagina = 5

#     def get_context_data(self, casa_id, **kwargs):
#         context = super().get_context_data(**kwargs)        
#         casa = Casa.objects.get(pk=casa_id)
#         registros = Registro.objects.filter(casa=casa).order_by('-data')
#         paginator = Paginator(registros, self.registros_por_pagina)
#         page = self.request.GET.get('page')

#         try:
#             registros_paginados = paginator.page(page)
#         except PageNotAnInteger:
#             registros_paginados = paginator.page(1)
#         except EmptyPage:
#             registros_paginados = paginator.page(paginator.num_pages)
#         context['casa'] = casa
#         context['registros'] = registros_paginados
#         return context

# class HistoricoCasa(ListView):
#     template_name = 'registro/historico1.html'
#     model = Registro
#     ordering = '-data'
#     paginate_by = 10

#     def get_context_data(self, casa_id, **kwargs):
#         context = super().get_context_data(**kwargs)
#         casa = Casa.objects.get(pk=casa_id)
#         registros = Registro.objects.filter(casa=casa).order_by('-data')
#         context['registros'] = registros
#         context['casa'] = casa
#         return context
    

class HistoricoCasa(LoginRequiredMixin, ListView):
    template_name = 'registro/historico1.html'
    model = Registro
    ordering = ['-data']
    paginate_by = 10

    def get_queryset(self):
        casa_id = self.kwargs.get('casa_id')
        casa = Casa.objects.get(pk=casa_id)
        queryset = Registro.objects.filter(casa=casa).order_by('-data')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        casa_id = self.kwargs.get('casa_id')
        casa = Casa.objects.get(pk=casa_id)
        context['casa'] = casa
        return context

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'user'
    
    
class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = get_user_model()
    form_class = RegistrationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')
    

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["casas"] = Casa.objects.all()[:1]
        return context

class Painel(LoginRequiredMixin, TemplateView):
    template_name = 'painel.html'

    def get_context_data(self, casa_id, **kwargs):
        context = super().get_context_data(**kwargs)        
        casa = Casa.objects.get(pk=casa_id)
        registros = Registro.objects.filter(casa=casa).order_by('-data')
        registro_recente = Registro.objects.latest('data')
        registro_oficial_recente = Registro.objects.filter(oficial=True).latest('data')
        diferenca_consumo = registro_recente.consumo - registro_oficial_recente.consumo
        ultima_data = registro_recente.data
        ultima_data_oficial = registro_oficial_recente.data
        dias = abs(ultima_data_oficial.day - ultima_data.day)        
        diferenca_injecao = registro_recente.injecao - registro_oficial_recente.injecao
        media_producao_diaria = diferenca_injecao // dias
        saldo = diferenca_injecao - diferenca_consumo
        prod_maxima = registro_oficial_recente.capacidade_maxima
        diferenca_ate_prod_max = prod_maxima - diferenca_injecao
        media_consumo_diario = diferenca_consumo // dias
        total = diferenca_consumo + diferenca_injecao
        context['diferenca_consumo'] = diferenca_consumo
        context['diferenca_injecao'] = diferenca_injecao
        context['diferenca_ate_prod_max'] = diferenca_ate_prod_max
        context['casa'] = casa
        context['registros'] = registros
        context['saldo'] = saldo        
        context['total'] = total   
        context['prod_maxima'] = prod_maxima   
        context['media_producao_diaria'] = media_producao_diaria
        context['media_consumo_diario'] = media_consumo_diario
        return context
    

@login_required
def grafico(request):
    return render(request, 'grafico.html')
