from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib import messages
from gestao.models import Casa, Registro, Usuario
from gestao.forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404



# Create your views here.

class LandingPage(TemplateView):
    template_name = 'landing_page.html'

class Sobre(TemplateView):
    template_name = 'quem-somos.html'

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
    
def DocumentCasa(request, casa_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=historico.pdf'
    p = canvas.Canvas(response)
    casa = Casa.objects.get(pk=casa_id)
    registros = Registro.objects.filter(casa=casa).order_by('-data')
    p.drawString(100, 800, f"Histórico da Casa: {casa.numero}")
    y = 780
    for registro in registros:
        y -= 20
        data_formatada = registro.data.strftime('%d/%m/%Y') 
        p.drawString(100, y, f"Data: {data_formatada}| Autor: {registro.autor}| Consumo: {registro.consumo}| Produção: {registro.injecao}")
    p.showPage()
    p.save()
    return response

class UserProfileView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'registration/profile.html'
    context_object_name = 'usuario'
    
    
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
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                context["msg"] = "Bem-vindo, Administrador!"
            else:
                usuario = self.request.user.usuario
                context["msg"] = "Bem-vindo, ao sistema administrativo!"
                context["casas"] = Casa.objects.filter(proprietario=usuario)[:1]
                casas_count = Casa.objects.filter(proprietario=usuario).count()
                context["casas_count"] = casas_count
        return context

    
class Painel(LoginRequiredMixin, TemplateView):
    template_name = 'painel.html'

    def dispatch(self, request, casa_id, *args, **kwargs):
        casa_atual = get_object_or_404(Casa, pk=casa_id)
        if request.user.usuario != casa_atual.proprietario:
            return render(request, 'adm/acesso-negado.html')       
        return super().dispatch(request, casa_id=casa_id, *args, **kwargs)

    def get_context_data(self, casa_id, **kwargs):
        context = super().get_context_data(**kwargs)  
        casa = Casa.objects.get(pk=casa_id)
        registros = Registro.objects.filter(casa=casa).order_by('-data')
        registro_recente = Registro.objects.filter(casa=casa).latest('data')
        registro_oficial_recente = Registro.objects.filter(casa=casa, oficial=True).latest('data')
        context['registro_oficial_recente'] = registro_oficial_recente    
        context['registro_recente'] = registro_recente

        if not registros.exists():
            return render(self.request, 'registro/cadastrar.html', context=context)    

        if registro_oficial_recente == registro_recente:
            context["msg"] = "Informações insuficientes para gerar um Painel! Insira dados e retorne!"           

        else:
            diferenca_consumo = registro_recente.consumo - registro_oficial_recente.consumo
            ultima_data = registro_recente.data
            ultima_data_oficial = registro_oficial_recente.data
            dias = abs((ultima_data_oficial - ultima_data).days)        
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
            context['dias'] = dias            

        return context
    
@login_required
def grafico(request):
    return render(request, 'grafico.html')
