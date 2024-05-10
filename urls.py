# sistema_reservas/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', include('reservas.urls')),  # Certifique-se de que esta linha está correta
    # Inclua outras configurações de URL conforme necessário
]