from rest_framework import serializers
from clinica.models import Paciente, Medico, Consulta, Especialidade
from clinica.validators import cpf_invalido, nome_invalido, celular_invalido


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self,dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa seguir o modelo: 86 99999-9999 (respeitando traços e espaços)'})
        return dados

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        exclude = []

class ListaConsultasPacienteSerializer(serializers.ModelSerializer):
    medico_nome = serializers.ReadOnlyField(source='medico.nome')
    especialidade = serializers.ReadOnlyField(source='medico.especialidade')
    data_hora = serializers.SerializerMethodField()
    
    class Meta:
        model = Consulta
        fields = ['medico_nome', 'especialidade', 'data_hora']
    
    def get_data_hora(self, obj):
        return obj.data_hora.strftime('%d/%m/%Y %H:%M')

class ListaConsultasMedicoSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.ReadOnlyField(source='paciente.nome')
    
    class Meta:
        model = Consulta
        fields = ['paciente_nome', 'data_hora']

        
class PacienteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id','nome','email','celular']