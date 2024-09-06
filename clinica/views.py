from clinica.models import Paciente, Medico, Consulta
from clinica.serializers import (
    PacienteSerializer, MedicoSerializer, ConsultaSerializer, 
    ListaConsultasPacienteSerializer, ListaConsultasMedicoSerializer, 
    PacienteSerializerV2
)
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from clinica.throttles import ConsultaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PacienteViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de pacientes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - PacienteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa PacienteSerializerV2.
    """
    queryset = Paciente.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return PacienteSerializerV2
        return PacienteSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de Médicos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Medico.objects.all().order_by("id")
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ConsultaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de Consultas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - ConsultaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    queryset = Consulta.objects.all().order_by("id")
    serializer_class = ConsultaSerializer
    throttle_classes = [UserRateThrottle, ConsultaAnonRateThrottle]
    http_method_names = ["get", "post"]


class ListaConsultasPaciente(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Consultas por id de Paciente
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Consulta.objects.filter(paciente_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaConsultasPacienteSerializer


class ListaConsultasMedico(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Consultas por id de Médico
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Consulta.objects.filter(medico_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaConsultasMedicoSerializer
