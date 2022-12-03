from django.contrib import admin

from .models import Client, Mailing, Message


class ClientAdmin(admin.ModelAdmin):
    """Класс отображения в админке задач"""
    list_display = ('id', 'phone', 'operator_code', 'tag', 'time_zone')
    list_display_links = ('id', 'phone', 'tag')
    search_fields = ('phone', 'tag')
    list_filter = ('phone', 'tag')
    empty_value_display = '-пусто-'
    
class MailingAdmin(admin.ModelAdmin):
    """Класс отображения в админке задач"""
    list_display = ('id', 'start_date', 'stop_date', 'message')
    list_display_links = ('id',)
    search_fields = ('start_date', 'stop_date')
    list_filter = ('start_date', 'stop_date')
    empty_value_display = '-пусто-'
    
class MessageAdmin(admin.ModelAdmin):
    """Класс отображения в админке задач"""
    list_display = ('id', 'create_date', 'status', 'mailing', 'client')
    list_display_links = ('id', 'mailing', 'client')
    search_fields = ('create_date', 'status', 'mailing', 'client')
    list_filter = ('create_date', 'status', 'mailing', 'client')
    empty_value_display = '-пусто-'


admin.site.register(Client, ClientAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(Message, MessageAdmin)
