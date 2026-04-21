from django.shortcuts import render
from django.http import JsonResponse
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list[any](tarefas), safe=False)

def listar_tarefas_abertas(request):
    tarefas_abertas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas_abertas), safe=False)   
