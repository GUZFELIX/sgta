from django.db import models
from usuarios.models import Usuario

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    PRIORIDADE_CHOICES = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não Urgente'),
    ]

    from django.db import models
from django.utils import timezone # Adicione esta importação
from usuarios.models import Usuario

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    PRIORIDADE_CHOICES = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não Urgente'),
    ]

    
    titulo = models.CharField(max_length=255, default='')
    descricao = models.TextField(default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    prioridade = models.CharField(max_length=15, choices=PRIORIDADE_CHOICES, default='NAO_URGENTE')
    data_criacao = models.DateTimeField(default=timezone.now) 
    data_entrega = models.DateField(default=timezone.now)
    
    usuario_responsavel = models.ForeignKey(
        Usuario, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.titulo