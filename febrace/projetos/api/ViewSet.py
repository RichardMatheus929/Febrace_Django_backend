from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from projetos.models import Projeto
from .Serializers import ProjetoSerializer

class ProjetoViewSet(ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
