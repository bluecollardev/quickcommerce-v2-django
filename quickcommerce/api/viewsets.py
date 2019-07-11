from quickcommerce.models import Product
from quickcommerce.models import Customer

from .serializers import productSerializer
from .serializers import customerSerializer

from rest_framework import viewsets

class productViewset(viewsets.ModelViewSet):
    """
    retrieve:
    Retorna um determinado produto

    list:
    Retorna a lista de todos os produtos.

    create:
    Cria um novo produto.

    update:
    Atualiza um produto por inteiro.

    partial_update:
    Atualiza apenas campos especificados no request de um determinado produto.

    destroy:
    Elimina um produto.
    """
    keycloak_scopes = {
        'GET': 'product:view',
        'POST': 'product:add',
        'PUT': 'product:update',
        'DELETE': 'product:delete',
        # 'PATCH': 'product:update',
    }
    queryset = Product.objects.all()
    serializer_class = productSerializer

class customerViewset(viewsets.ModelViewSet):
    """
    retrieve:
    Retorna um determinado produto

    list:
    Retorna a lista de todos os produtos.

    create:
    Cria um novo produto.

    update:
    Atualiza um produto por inteiro.

    partial_update:
    Atualiza apenas campos especificados no request de um determinado produto.

    destroy:
    Elimina um produto.
    """
    keycloak_scopes = {
        'GET': 'customer:view',
        'POST': 'customer:add',
        'PUT': 'customer:update',
        'DELETE': 'customer:delete',
        # 'PATCH': 'customer:update',
    }
    queryset = Customer.objects.all()
    serializer_class = customerSerializer
