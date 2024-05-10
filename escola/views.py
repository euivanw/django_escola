from rest_framework import viewsets, generics

from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, \
    ListaAlunosMatriculadosSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibir todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """ Exibir todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """ Exibir todas as matrículas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAlunoViewSet(generics.ListAPIView):
    """ Exibir todos as matrículas de um aluno """
    serializer_class = ListaMatriculasAlunoSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset


class ListaAlunosMatriculadosViewSet(generics.ListAPIView):
    """ Exibir todos os alunos matriculados em um curso """
    serializer_class = ListaAlunosMatriculadosSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
