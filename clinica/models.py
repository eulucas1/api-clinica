from django.db import models
from django.core.validators import MinLengthValidator


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3)])
    especialidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Consulta de {self.paciente.nome} com {self.medico.nome} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
