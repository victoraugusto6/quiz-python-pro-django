from django.contrib import admin

# Register your models here.
from quiz.base.models import Pergunta, Aluno, Resposta


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'enunciado', 'disponivel')
    ordering = ('id',)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'criado_em')
    ordering = ('id',)


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('respondida_em', 'aluno', 'pergunta', 'pontos')
    ordering = ('id',)
