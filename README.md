# API REST com Django
Esta é uma API RESTful construída utilizando Django e Django REST Framework. O projeto inclui funcionalidades avançadas como autenticação, permissões, validações, paginação, filtros, versionamento, documentação, e deploy na AWS.

## Tecnologias Utilizadas
- **Django 5.0.3**
- **Django REST Framework**
- **SQLite3** (padrão, mas facilmente configurável para outros bancos de dados)
- **django-filters** (para filtros avançados)
- **drf-yasg** (para documentação automática da API)
- **CORS Headers** (para permitir o acesso a partir de domínios externos)
- **AWS** (deploy em produção)
- **Docker** (opcional para ambientes de desenvolvimento e produção)

## Funcionalidades
- **Validação de dados**
- **Paginação e Ordenação**
- **Versionamento de API**
- **Autenticação com DjangoModelPermissions**
- **Limitação de requisições (Throttling)**
- **CORS configurado**
- **Documentação automática da API usando Swagger**
  
## Requisitos
- **Python 3.9+**
- **Django 5.0.3**
- **virtualenv** (para gerenciamento de ambientes virtuais)

## Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/eulucas1/api-clinica.git
cd api-clinica
```

### 2. Criar e ativar o ambiente virtual
Com **virtualenv**:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar o banco de dados
O banco padrão é SQLite, mas você pode configurar outro banco de dados no arquivo `settings.py`.

Rodar as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Rodar o servidor local
```bash
python manage.py runserver
```

Acesse a API localmente em `http://127.0.0.1:8000/`.

## Documentação da API
A documentação da API pode ser acessada no Swagger através da rota:
```
/swagger/
```

## Deploy
Para realizar o deploy na AWS, segui os passos para configuração de uma instância EC2: [Deploy de uma aplicação Django na AWS](https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/create-deploy-python-django.html).

## Próximos Passos de Desenvolvimento

### 1. Conclusão da Integração com o Front-End
O próximo passo é finalizar a integração da API com o [front-end](https://github.com/eulucas1/front-clinica). A API será consumida por uma Single Page Application (SPA) desenvolvida com REACT + VITE

### 2. Implementação de Testes Unitários e Automatizados
Também está planejada a implementação de testes unitários e automatizados para garantir a qualidade e confiabilidade da API. Serão utilizados frameworks como **Django Test Framework** e **Pytest** para escrever e executar os testes de unidades e de integração. A cobertura de testes será monitorada para garantir que todas as funcionalidades críticas estejam cobertas.

Objetivos principais:
- Garantir a funcionalidade correta dos endpoints
- Validar as permissões e autenticação
- Testar a paginação, filtros e versionamento
- Testar o controle de requisições (throttling)
- Automatizar a execução de testes nos pipelines de CI/CD
