# Create your views here.

from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'adicionar_tarefa.html', {'form': form})
