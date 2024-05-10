# sistema_reservas/reservas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_espacos, name='lista_espacos'),  # Exemplo de rota
    # Adicione outras rotas conforme necessário
]