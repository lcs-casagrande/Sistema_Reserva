from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .models import Espaco
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Conta criada para {username}!')
            return redirect('home')  # Substitua 'home' pelo nome do seu URL de índice ou dashboard
    else:
        form = UserRegisterForm()
    return render(request, 'reservas/register.html', {'form': form})


def lista_espacos(request):
    espacos = Espaco.objects.all()
    return render(request, 'reservas/lista_espacos.html', {'espacos': espacos})
def nova_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('algum_url')  # Substitua 'algum_url' pelo destino após a reserva
    else:
        form = ReservaForm()
    return render(request, 'reservas/nova_reserva.html', {'form': form})


def home(request):
    return render(request, 'home.html')