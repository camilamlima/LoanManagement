from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Client
from .serializers import ClientSerializer


class ClientViewAll(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        client_id = get_object_or_404(
            Client, client_id = self.request.data.get('client_id')
        )
        return serializer.save(client_id=client_id)


class ClientIdView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


def test(request):
    return redirect('http://google.com.br')
