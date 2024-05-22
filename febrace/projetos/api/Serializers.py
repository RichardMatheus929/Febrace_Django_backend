from rest_framework.serializers import ModelSerializer
from projetos.models import Projeto

class ProjetoSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = ('nome',
                  'categoria_premiacao',
                  'escola',
                  'cidade',
                  'estado',
                  'ano'
                  )