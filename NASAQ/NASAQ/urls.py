"""NASAQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth
from django.urls import path, include
from apps.usuarios import views as v
from apps.categorias import views as c
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name= 'home'),
    path('nosotros/', views.Nosotros, name= 'nosotros'),
    path('login/', auth.LoginView.as_view(template_name = 'usuarios/login.html'), name= 'login'),
    path('logout/', auth.LogoutView.as_view(), name = 'logout'),
    path('registro/', v.Registro, name='registro'),
    path('juego/', views.Juego, name='juego'),
    path('nasacos/', include('apps.categorias.urls')),
    path('partida/', include('apps.juego.urls')),
]

