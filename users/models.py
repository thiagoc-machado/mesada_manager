from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    valor_mesada = models.DecimalField(max_digits=10, decimal_places=2)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    data_criacao = models.DateField()
    data_pagamento = models.DateField()

    def __str__(self): 
        return self.user.username

class Mesada(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField()
    data_pagamento = models.DateField()
    descontos = models.DecimalField(max_digits=10, decimal_places=2)
    acrescimos = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('mesada-detail', kwargs={'pk': self.pk})
    
class Historico_mesada(models.Model):
    mesada = models.ForeignKey(Mesada, on_delete=models.CASCADE)
    data_criacao = models.DateField()
    data_pagamento = models.DateField()
    descontos = models.DecimalField(max_digits=10, decimal_places=2)
    acrescimos = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.mesada.nome
    
    def get_absolute_url(self):
        return reverse('historico-detail', kwargs={'pk': self.pk})
