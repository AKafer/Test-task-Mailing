import time
import requests
from datetime import datetime
import logging
import sys
import pytz
from django.core.management import BaseCommand

from mailing.models import Mailing, Message
from http import HTTPStatus

utc = pytz.UTC

TIME_SLEEP = 5
ENDPOINT = 'https://probe.fbrq.cloud/v1'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'\
    'eyJleHAiOjE3MDE1MDk2NzcsImlzcyI6ImZhYnJpc'\
    'XVlIiwibmFtZSI6IkFLYWZlcjgyIn0.ANuZGTpP_X'\
    'nUXUTiZC1UKdFB8yo5M9UTW1y2RbmY58E'
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

logging.basicConfig(
        level=logging.INFO,
        format=(
            '%(asctime)s - [%(levelname)s][%(lineno)s][%(filename)s]'
            '[%(funcName)s]- %(message)s'
        ),
        handlers=[logging.StreamHandler(sys.stdout)]
    )


class Command(BaseCommand):

    def create_messages(self, task):
        print(task.message)
        new_messages = [
            Message(
                create_date=datetime.today().replace(tzinfo=utc),
                status='created',
                mailing=task,
                client=client
            )
            for client in task.clients.all()
        ]
        Message.objects.bulk_create(new_messages)

    def mes_status(self, message, status):
        message.status = status
        message.save()
        
    def edit_status(self, task):
        messages = Message.objects.filter(mailing=task)
        for message in messages:
            if message.status == 'created':
                self.mes_status(message, 'send_fail')

    def mailing(self, task):
        messages = Message.objects.filter(mailing=task)
        for message in messages:
            if (task.stop_date.replace(tzinfo=utc)
                    < datetime.today().replace(tzinfo=utc)):
                return 'Рассылка не завершена'
            data = {
                "id": message.id,
                "phone": message.client.phone,
                "text": task.message
            }
            try:
                logging.info(
                    f'Отправляю сообщение {message.id} к внешнему API'
                )
                response = requests.post(
                    ENDPOINT + f'/send/{message.id}',
                    headers=HEADERS, json=data
                )
                if response.status_code != HTTPStatus.OK:
                    raise ConnectionError
                if response.json()['message'] == 'OK':
                    self.mes_status(message, 'send_success')
                else:
                    self.mes_status(message, 'send_fail')
            except ConnectionError:
                logging.error('Сбой при запросе к эндпоинту')
                self.mes_status(message, 'send_fail')
        return 'Рассылка завершена'

    def handle(self, *args, **kwargs):
        logging.info('Программа рассылок запущена')
        while True:
            tasks = Mailing.objects.all()
            for task in tasks:
                if (task.status
                    and task.start_date.replace(tzinfo=utc)
                        < datetime.today().replace(tzinfo=utc)):
                    logging.info(f'Начинаю рассылку {task.id}')
                    self.create_messages(task)
                    mailing_status = self.mailing(task)
                    if mailing_status == 'Рассылка не завершена':
                        self.edit_status(task)
                        logging.info(f'Рассылка {task.id} не завершена вовремя')
                    else:
                        logging.info(f'Рассылка {task.id} завершена вовремя')
                    task.status = False
                    task.save()
            time.sleep(TIME_SLEEP)
