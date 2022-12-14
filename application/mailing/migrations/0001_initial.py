# Generated by Django 4.1.3 on 2022-12-02 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('operator_code', models.IntegerField()),
                ('tag', models.CharField(max_length=11)),
                ('time_zone', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Старт рассылки')),
                ('stop_date', models.DateTimeField(verbose_name='Стоп рассылки')),
                ('message', models.TextField()),
                ('clients', models.ManyToManyField(related_name='clients', to='mailing.client', verbose_name='клиенты')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(verbose_name='Время создания')),
                ('status', models.CharField(choices=[('created', 'created'), ('send_success', 'send_success'), ('send_fail', 'send_fail')], default='created', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='mailing.client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailing', to='mailing.mailing')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
