# lista/urls.py
from django.urls import path
from .views import lista_tarefas, adicionar_tarefa

urlpatterns = [
    path('lista_tarefas/', lista_tarefas, name='lista_tarefas'),
    path('adicionar_tarefa/', adicionar_tarefa, name='adicionar_tarefa'),
    # Adicione outras URLs conforme necessário
]

