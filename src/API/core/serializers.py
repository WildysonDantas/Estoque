from rest_framework import routers, serializers, viewsets
from .models import Estoque, Historico

#criando um representacao serializer do meu model Estoque

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ('fk_codigo', 'entrada', 'saida', 'quantidade')


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ('fk_codigo', 'entrada', 'quantidade')

class SaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ('fk_codigo', 'saida', 'quantidade',)


class EstoqueSerializer(serializers.ModelSerializer):
    movimentacao = HistoricoSerializer(many=True,read_only=True)
    
    class Meta:
        model = Estoque
        fields = ('codigo', 'nome', 'quantidade', 'categoria','movimentacao')


       


