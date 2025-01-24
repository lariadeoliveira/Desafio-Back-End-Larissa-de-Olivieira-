from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Campos adicionais para o modelo de usuário
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Transferencia(models.Model):
    remetente = models.ForeignKey(Usuario, related_name='transferencias_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Usuario, related_name='transferencias_recebidas', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_transferencia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transferência de {self.remetente.username} para {self.destinatario.username} - R$ {self.valor}'