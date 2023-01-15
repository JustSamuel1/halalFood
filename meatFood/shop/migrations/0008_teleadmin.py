# Generated by Django 4.1.4 on 2022-12-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_order_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeleAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('chat_id', models.CharField(max_length=15)),
                ('confirmed_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
