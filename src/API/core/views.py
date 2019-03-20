
from django.shortcuts import render
import datetime
from .models import Estoque, Historico
from rest_framework.views import APIView
from .serializers import EstoqueSerializer, HistoricoSerializer, SaidaSerializer, EntradaSerializer
from rest_framework.permissions import IsAuthenticated, BasicAuthentication


class EstoqueViewSet(APIView): #index
    ''' Controle de Estoque'''
    def get(self, request):
        return render(request, 'index.html', {})

        
class cadastroMercadoria(APIView): #Classe responvel por realizar o cadastro do estoque
    permission_classes = (IsAuthenticated,)
    #Metodo para coletar as informacoes do formulario e rendereizar na pagina
    def get(self, request):
        print( datetime.datetime.now())
        style = {'template_pack': 'rest_framework/vertical/'} #utilizando do template vertical nativo do django
        form = EstoqueSerializer()
        return render(request, 'cadastro.html', {'form': form,'style': style})

    #No metodo post, foi verificado se o formulario é valido antes de salvar os dados
    #Uma mensagem é exibida ao usuario caso a operacao tenha dado errado ou certo
    def post(self, request):
        form = EstoqueSerializer()
        style = {'template_pack': 'rest_framework/vertical/'}
        sucesso = 'Dados Salvos com suceso'
        error = 'Ocorreu um erro ao realizar essa transação. Verifique sua conexao com a internet'
    
        serializer = EstoqueSerializer(data=request.data) #Coletando as informacoes enviadas pelo usuario
        if serializer.is_valid():
            serializer.save()
            est = Estoque.objects.all()
            cont = len(est)
            cont = cont - 1
            cod = est[cont].codigo
            qtd = request.data['quantidade']
            Historico.objects.create(fk_codigo=est[cont], entrada = datetime.datetime.now(), quantidade=qtd)
            return render(request, 'cadastro.html', {'form': form,'style': style,'msg': sucesso})
        else:
            return render(request, 'cadastro.html', {'form': form,'style': style,'msg': error})


class entrada(APIView): #classe responvavel pelo registro de entrada do estoque
    permission_classes = (IsAuthenticated,)
    def get( self, request):
        style = {'template_pack': 'rest_framework/vertical/'}
        form = EntradaSerializer() #Coletando o historico de entrada
        return render(request, 'entrada.html',  {'form': form,'style': style})
    def post(self, request):
        form = HistoricoSerializer()
        style = {'template_pack': 'rest_framework/vertical/'}
        sucesso = 'Dados Salvos com suceso'
        error = 'Ocorreu um erro ao realizar essa transação. Verifique sua conexao com a internet'

        serializer = HistoricoSerializer(data=request.data) #Coletando as informacoes enviadas pelo usuario
        if serializer.is_valid():
            a = Estoque.objects.filter(codigo=request.data['fk_codigo']) #trecho de codigo responsavel pela adicao ao estoque
            qt = a[0].quantidade
            add = codigo=request.data['quantidade']
            a.update(quantidade=qt+int(add)) #atualizando a tabela do banco de dados
            serializer.save()

            return render(request, 'entrada.html', {'form': form,'style': style,'msg': sucesso})
        else:
            return render(request, 'entrada.html', {'form': form,'style': style,'msg': error})


class saida(APIView): #Classe responvel pelo registro de saida do etoque
    permission_classes = (IsAuthenticated,)
    def get( self, request):
        style = {'template_pack': 'rest_framework/vertical/'}
        form = SaidaSerializer()
        return render(request, 'saida.html',  {'form': form,'style': style})

    def post(self, request):
        form = HistoricoSerializer()
        style = {'template_pack': 'rest_framework/vertical/'}
        sucesso = 'Dados Salvos com suceso'
        error = 'Ocorreu um erro ao realizar essa transação'
    
        serializer = HistoricoSerializer(data=request.data) #Coletando as informacoes enviadas pelo usuario
        if serializer.is_valid():

            a = Estoque.objects.filter(codigo=request.data['fk_codigo']) #trecho de codigo responsavel por diminui da tabela estoque
            qt = a[0].quantidade
            sub = codigo=request.data['quantidade']
            if int(sub) > qt: #realizando o teste da subrtacao ser menor do que o estoque
                return render(request, 'saida.html', {'form': form,'style': style,'msg': 'Error: Quantidade Excede o estoque'})
            else:
                a.update(quantidade=qt-int(sub))
                serializer.save()
                return render(request, 'saida.html', {'form': form,'style': style,'msg': sucesso})
        else:
            return render(request, 'saida.html', {'form': form,'style': style,'msg': error})



def movimentacao(request): #metodo responsavel por exibir as opcoes de registro

    return render(request, 'movimentacao.html', {})
class ConsultaEstoque(APIView): #classe responsavel pela consulta
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        queryset = Historico.objects.all() # pegando as informacoes do historico
        return render(request, 'consulta.html', {'estoque': queryset, 'queryset':  getHistorico()})

    def post(self, request):

        a = request.POST['codigo']
        estoque = Estoque.objects.filter(nome=a) #Trecho responsavel pela consuylta no banco de dados
        cd = estoque[0].codigo
        data = Historico.objects.filter(fk_codigo=cd) #cruazando os dados com o historico
        return render(request, 'consulta.html', {'queryset':  getHistorico(), 'estoque': data})


def getHistorico():
    queryset = Historico.objects.all() # pegando as informacoes do historico
    nome = []
    for x in queryset:
        if x.fk_codigo not in nome:
            nome.append(x.fk_codigo)
    return nome
