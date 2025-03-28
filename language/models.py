from django.db import models
from django.contrib.auth.models import User

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
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Professor: {self.user.username}"
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
    Teacher,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="students"
    )


    def __str__(self):
        return f"Estudante: {self.user.username}"
    

class Topico(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

class Resposta(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, related_name='respostas')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resposta de {self.autor} em {self.topico.titulo}"