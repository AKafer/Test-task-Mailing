import pytz
from rest_framework import serializers

from mailing.models import Client, Mailing, Message

utc = pytz.UTC


class ClientSerializer(serializers.ModelSerializer):
    """Класс сериализатора файлов."""

    class Meta:
        fields = '__all__'
        model = Client


class MailingSerializer(serializers.ModelSerializer):
    """Класс сериализатора файлов."""
    phones = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Mailing

    def get_phones(self, obj):
        """Функция определения статуса задачи."""
        phones = []
        for client in obj.clients.all():
            phones.append(client.phone)
        return phones


class MessageSerializer(serializers.ModelSerializer):
    """Класс сериализатора файлов."""
    phone = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Message

    def get_phone(self, obj):
        """Функция определения статуса задачи."""
        return obj.client.phone
