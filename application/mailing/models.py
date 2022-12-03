from django.db import models


class Client(models.Model):
    """
    Класс клиента.
    """
    phone = models.CharField(max_length=11)
    operator_code = models.CharField(max_length=11)
    tag = models.CharField(max_length=11)
    time_zone = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.phone


class Mailing(models.Model):
    """
    Класс рассылки.
    """
    
    start_date = models.DateTimeField('Старт рассылки')
    stop_date = models.DateTimeField('Стоп рассылки')
    message = models.TextField()
    clients = models.ManyToManyField(
        Client,
        related_name='clients',
        verbose_name='клиенты'
    )
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.message
    

class Message(models.Model):
    """
    Класс сообщения.
    """
    CHOICES = (
        ('created', 'created'),
        ('send_success', 'send_success'),
        ('send_fail', 'send_fail'),
    )
    
    create_date = models.DateTimeField('Время создания')
    status = models.CharField(max_length=30, choices=CHOICES, default='created')
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, related_name='mailing')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='client')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.status