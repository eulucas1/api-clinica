from django.contrib import admin
from django.urls import path,include
from clinica.views import PacienteViewSet,MedicoViewSet, ConsultaViewSet, ListaConsultasPaciente,ListaConsultasMedico
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API",
      default_version='v1',
      description="Documentação da API Clínica",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('pacientes', PacienteViewSet, basename='Pacientes')
router.register('medicos', MedicoViewSet, basename='Medicos')
router.register('consultas', ConsultaViewSet, basename='Consultas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('pacientes/<int:pk>/consultas/', ListaConsultasPaciente.as_view()),
    path('medicos/<int:pk>/consultas/', ListaConsultasMedico.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
