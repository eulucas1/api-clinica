from django.contrib import admin
from clinica.models import Paciente, Especialidade, Medico, Consulta

class PacientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(Paciente, PacientesAdmin)

class MedicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm', 'especialidade')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome', 'crm',)

admin.site.register(Medico, MedicosAdmin)

class ConsultasAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'data_hora')
    list_display_links = ('id',)
    list_per_page = 20
    search_fields = ('paciente__nome', 'medico__nome',)

admin.site.register(Consulta, ConsultasAdmin)

class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)

admin.site.register(Especialidade, EspecialidadesAdmin)
