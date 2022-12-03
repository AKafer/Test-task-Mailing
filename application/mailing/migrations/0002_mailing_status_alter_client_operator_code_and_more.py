# Generated by Django 4.1.3 on 2022-12-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='operator_code',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('send_success', 'send_success'), ('send_fail', 'send_fail')], default='created', max_length=30),
        ),
    ]
