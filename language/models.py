from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class Material(models.Model):
    # Opções para o tipo de material
    TIPO_MATERIAL = [
        ('PDF', 'PDF'),
        ('OUTROS', 'Outros Tipos'),
    ]
    
    nome = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='materiais/')
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_MATERIAL,
        default='PDF'
    )
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)  # Data de envio automática

    def __str__(self):
        return f"Mensagem de {self.nome} ({self.email})"
    
class Video(models.Model):
    titulo = models.CharField(max_length=100)
    modulo = models.CharField(max_length=100, default="Módulo 1")  # Valor padrão
    ordem = models.IntegerField(default=1)  # Ordem da aula dentro do módulo
    arquivo = models.FileField(upload_to='videos/')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relação 1 para 1 com o User
    is_teacher = models.BooleanField(default=False)  # True para professor, False para estudante

    def __str__(self):
        return f"Perfil de {self.user.username}"