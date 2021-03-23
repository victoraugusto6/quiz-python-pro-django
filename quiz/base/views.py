from django.shortcuts import render

from quiz.base.models import Pergunta


def home(request):
    return render(request, 'base/home.html')


def classificacao(request):
    return render(request, 'base/classificacao.html')


def perguntas(request, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    contexto = {'indice_da_questao': indice, 'pergunta': pergunta}
    return render(request, 'base/game.html', context=contexto)
