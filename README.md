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
`pip install django`
``` python
from tal im0ot tal
```

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


# Como usar? (Modo usuário)
O usuário pode fazer o uso da aplicação clicando no link (https://web-wine-iota.vercel.app/). Logo na sequência o mesmo terá está visão da aplicação com a tela inicial de usuário.
![Tela inicial](image.png)
Na imagem acima, existe um campo de escrita logo no topo onde o usuário irá digitar o nome da sua tarefa e em seguida clicar no botão "ADICIONAR". Feito isso, a sua primeira tarefa estará gravada e a mesma aparecerá no topo da lista.

A nossa lista de tarefas aparece logo abaixo do campo de adição de novas tarefas, nele é possível ver as tarefas já registradas, concluidas e em aberto. (veja a imagem a seguir).

![Lista](image-1.png)

Com finalidade ilustrativa, existem na imagem tarefas em aberto e tarefas concluídas. 
Como descrito no item anterior, cada nova tarefa adcionada aparecerá no topo da lista.
Assim que terminada a sua tarefa o usuário clica no botão amarelo, isso fara com que a sua tarefa seja riscada da lista e considerada como concluída.

![Tarefa concluida](image-2.png)

O icone vermelho com um x, indica que o usuário pode excluir aquela tarefa. Portanto, feito isso, ela será deletada permanentemente da sua lista.

![Botão de exclusão](image-3.png)

Para isso, não necessariamente a tarefa precisa estar concluída.

# Como usar? (Modo Administrador)

a Imagem abaixo mostra como é a tela de um usuário administrador.

![Tela login admin](image-4.png)

O administrador deverá logar usando seu nome de usuário e senha e em seguida clicar no botão "AVANÇAR". 

Em seguida ele verá a tela inicial de administrador:

![tela principal admin](image-5.png)

No canto superior direito são disponibilizadas ao administrador os seguintes campos e funcionalidades:
- Campo de boas vindas com o nome do administrador;
- Campo para ir direto ao site;
  - Ao clicar, o administrador será encaminhado para a tela inicial da aplicação.
- Campo para alterar senha;
  - Ao clicar, será aberta a janela para alteração de senha (imagem abaixo).

  ![Alterar senha](image-6.png)

    - O sistema pedirá a senha antiga do usuário.
    - o campo de nova senha deverá ser preenchido seguindo as orientações impostas. No campo seguite pede-se que repita a nova senha a ser cadastrada. 
    - POr fim o administrador clica no botão "ALTERAR MINHA SENHA". Sendo redirecionado para a pagina inicial de administrador.

- Campo para encerrar a sessão;
  - Ao clicar neste campo, o admin terá a sua frente a seguinte tela.

  ![Encerrar sessão](image-7.png)

Abaixo, no canto direito da tela são exibidos os campos: 

![Administração](image-8.png)

  - Aqui o user admin 


# Executar o servidor de desenvolvimento
python manage.py runserver ``

Visite http://127.0.0.1:8000/ em seu navegador da web para ver o aplicativo Lista de Tarefas em ação.







