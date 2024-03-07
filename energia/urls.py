"""
URL configuration for energia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .views import UserProfileView, Home, HistoricoCasa, Painel, grafico, RegistrationView
from gestao.views import NovaCasa, Casas, ApagarCasa, AtualizarCasa, DetalharCasa, NovoRegistro, Registros, DetalharRegistro, AtualizarRegistro, ApagarRegistro, NovoRegistroDaCasa

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', Home.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('historico_casa/<int:casa_id>/', HistoricoCasa.as_view(), name='historico'),
    path('painel/<int:casa_id>/', Painel.as_view(), name='painel'),
    path('adicionar-registro/<int:casa_id>', NovoRegistroDaCasa, name='registrar-registro'),
    path('grafico/', grafico, name='registrar-registro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', RegistrationView.as_view(), name='registration'),

    # ---------- URLs relacionadas à classe Casa ---------------

    path('nova-casa/', NovaCasa.as_view(), name='cadastrar-casa'),
    path('casas/', Casas.as_view(), name='casas'),
    path('apagar_casa/<int:pk>/', ApagarCasa.as_view(), name='apagar-casa'),
    path('atualizar_casa/<int:pk>/', AtualizarCasa.as_view(), name='atualizar-casa'),
    path('detalhar_casa/<int:pk>/', DetalharCasa.as_view(), name='detalhar-casa'),
    # path('detalhar_registro/<int:casa_id>/', detalhar_registro, name='detalhar_registro'),

    # ---------- URLs relacionadas à classe Registro ---------------

    path('novo-registro/', NovoRegistro.as_view(), name='cadastrar-registro'),
    path('registros/', Registros.as_view(), name='registros'),
    path('detalhar_registro/<int:pk>/', DetalharRegistro.as_view(), name='detalhar-registro'),
    path('atualizar_registro/<int:pk>/', AtualizarRegistro.as_view(), name='atualizar-registro'),
    path('apagar_registro/<int:pk>/', ApagarRegistro.as_view(), name='apagar-registro'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)