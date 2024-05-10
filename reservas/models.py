from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


    class Reserva(models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE)
        espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
        data_inicio = models.DateTimeField()
        data_fim = models.DateTimeField()

    def __str__(self):
        return f'{self.espaco.nome} reservado por {self.usuario.username}'

    from django.db import models

    class Espaco(models.Model):
        nome = models.CharField(max_length=100)
        descricao = models.TextField()
        capacidade = models.IntegerField()

        def __str__(self):
            return self.nome