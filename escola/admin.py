from django.contrib import admin

from escola.models import Aluno, Curso, Matricula


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento',)
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome',)


admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao',)
    list_display_links = ('id', 'codigo_curso',)
    list_per_page = 20
    search_fields = ('codigo_curso',)


admin.site.register(Curso, Cursos)


class Mastriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)
    list_per_page = 20


admin.site.register(Matricula, Mastriculas)
