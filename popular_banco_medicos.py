import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from clinica.models import Medico
fake = Faker('pt_BR')

estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

medicos_dados = [
    ('Dr. Carlos Silva', 'Cardiologia'),
    ('Dra. Maria Santos', 'Pediatria'),
    ('Dr. João Oliveira', 'Neurologia'),
    ('Dra. Ana Costa', 'Ortopedia'),
    ('Dr. Pedro Lima', 'Oftalmologia')
]

def gerar_crm():
    """Função para gerar CRM no formato UF + 6 dígitos (ex: SP123456)"""
    uf = random.choice(estados)
    numeros = str(random.randint(100000, 999999))  
    return f"{uf}{numeros}"

def criar_medicos():
    for nome, especialidade in medicos_dados:
        crm = gerar_crm()
        Medico.objects.create(nome=nome, crm=crm, especialidade=especialidade)

criar_medicos()
