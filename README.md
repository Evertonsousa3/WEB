# Aplicativo de Lista de Tarefas com Django e htmx 

## Visão Geral
Este é um aplicativo simples de Lista de Tarefas construído usando o framework web Django e a biblioteca htmx para uma interação dinâmica entre cliente e servidor. O aplicativo permite aos usuários gerenciar suas tarefas de forma dinâmica, sem a necessidade de código JavaScript complexo.

## Pré-requisitos
Antes de começar o tutorial, certifique-se de ter os seguintes pré-requisitos:

Compreensão básica de Python e do Framework Django.
Python (versão 3.6 ou superior) e pip instalados no seu sistema.
Familiaridade com o Django e seus conceitos.
[Nota: Use um ambiente virtual para a melhor prática. 👍]

## Passos
### 1. Instalar o Framework Django
Para começar a construir nosso simples aplicativo htmx, vamos configurar um novo projeto Django. Siga estas etapas para configurar a estrutura do Django:



### Instale o Framework Django usando o pip:
`` pip install django

# Crie um novo projeto Django:
django-admin startproject myproject

# Crie um novo aplicativo Django dentro do seu projeto:
cd myproject
python manage.py startapp myapp``

### 2. Configurar o Django
Abra o arquivo settings.py do seu projeto Django e adicione as seguintes linhas:

`` # settings.py

INSTALLED_APPS = [
    # ...
    'myapp',
]

TEMPLATES = [
    {
        'DIRS': ['templates'],
    },
]
``

### 3. Adicionar URLs
No myproject/urls.py, adicione as seguintes linhas:

`` # myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
] ``
Crie um arquivo chamado urls.py dentro da pasta myapp com o seguinte conteúdo:

`` # myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]

htmxpatterns = [
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('mark_todo/<int:pk>/', views.mark_todo, name='mark_todo'),
]

urlpatterns += htmxpatterns ``

### 4. Adicionar Modelo Todo
Abra o arquivo models.py dentro da pasta myapp e adicione o seguinte código:

`` # myapp/models.py

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title ``

### 5. Adicionar Funções de Visualização
Abra o arquivo views.py dentro da pasta myapp e adicione as funções de visualização:

`` # myapp/views.py

from django.shortcuts import render
from .models import Todo

def index(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'index.html', {'todos': todos})

def create_todo(request):
    title = request.POST.get('title')
    todo = Todo.objects.create(title=title)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

def mark_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos}) ``

### 6. Criar Templates
Crie uma pasta chamada templates dentro da pasta myproject. Dentro da pasta templates, crie um arquivo chamado base.html com o seguinte conteúdo:

`` <!-- myproject/templates/base.html -->

{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Conteúdo do head... -->
  </head>
  <body>
    <div class="container mt-5">
      {% block content %}
      {% endblock %}
    </div>

    <!-- Scripts do Bootstrap e htmx... -->

    {% block js_script %}
    {% endblock %}
  </body>
</html> ``

Crie um arquivo chamado index.html dentro da pasta templates com o seguinte conteúdo:

`` <!-- myproject/templates/index.html -->

{% extends 'base.html' %}
{% block title %} Home {% endblock %}
{% block content %}
  <!-- Conteúdo para a página inicial... -->
{% endblock %}
{% block js_script %}
  <script>
    document.body.addEventListener('htmx:configRequest', (event) => {
      event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
    })
  </script>
{% endblock %} ``

Crie um arquivo chamado todo-list.html dentro da pasta templates com o seguinte conteúdo:

`` <!-- myproject/templates/todo-list.html -->

{% if todos %}
  <!-- Conteúdo para a lista de tarefas... -->
{% else %}
  <h5>Atualmente, você não tem nenhuma tarefa.</h5>
{% endif %} ``

##7. Testar e Executar

Abra a interface de linha de comando e navegue até o diretório raiz do seu projeto Django. Execute os seguintes comandos:

`` # Aplicar migrações
python manage.py makemigrations
python manage.py migrate

# Executar o servidor de desenvolvimento
python manage.py runserver ``

Visite http://127.0.0.1:8000/ em seu navegador da web para ver o aplicativo Lista de Tarefas em ação.







