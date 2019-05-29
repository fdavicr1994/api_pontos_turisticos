from rest_framework.serializers import ModelSerializer
from atracaos.models import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao','horario_func','idade_minima','foto')