from django_filters import rest_framework as dfilters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from mailing.models import Client, Mailing, Message

from .filters import TagOperatorFilter
from .serializers import ClientSerializer, MailingSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """Класс представления клиентов"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (dfilters.DjangoFilterBackend,)
    filterset_class = TagOperatorFilter


class MailingViewSet(viewsets.ModelViewSet):
    """Класс представления рассылок"""
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """Класс представления сообщений"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('mailing', )
