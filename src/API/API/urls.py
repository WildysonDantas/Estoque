from django.contrib import admin
from django.urls import path, include
from core.views import cadastroMercadoria, EstoqueViewSet, movimentacao, ConsultaEstoque, entrada, saida

#from core.views import UpdateField
from rest_framework import routers
from core import views



#router = routers.DefaultRouter()
#router.register(r'estoque', EstoqueViewSet)
#router.register(r'update', UpdateField)


#router.register(r'update', UpdateField)

urlpatterns = [
    path('', EstoqueViewSet.as_view(), name='Estoque'),
    path('cadastro/', cadastroMercadoria.as_view(), name='Cadastro'),
    path('movimentacao/', views.movimentacao, name='Movimentacao'),
    path('consulta/', ConsultaEstoque.as_view(), name='Consulta'),
    path('registroentrada/', entrada.as_view(), name='REntrada'),
    path('registrosaida/', saida.as_view(), name='RSaida'),

    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
