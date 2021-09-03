from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)

from .models import Sale, SaleDetail

from .serializers import (
    VentaReporteSerializer,
    ProcesoVentaSerializer
)


class ReportVentasLista(ListAPIView):
    serializer_class = VentaReporteSerializer

    def get_queryset(self):
        return Sale.objects.all()


class RegistrarVenta(CreateAPIView):
    """ """
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = ProcesoVentaSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProcesoVentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tipo_recibo = serializer.validated_data['type_invoce']
        print('***********', tipo_recibo)
        return None
