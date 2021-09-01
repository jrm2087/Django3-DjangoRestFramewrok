from rest_framework.generics import (ListAPIView)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from django.shortcuts import render

from .serializers import ProductSerializer

from .models import Product


class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    # IsAdminUser, ReadOnly, IsAuthenticated
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        return Product.objects.productos_por_usuario(usuario)


class ListProductStok(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Product.objects.productos_con_stok()


class ListProducGenero(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        genero = self.kwargs['gender']
        return Product.objects.productos_por_genero(genero)
