# Generated by Django 3.2 on 2022-08-17 13:02

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]
