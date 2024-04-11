# Generated by Django 5.0.2 on 2024-04-11 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IcecreamShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icecreams', to='app.icecreamshop')),
            ],
        ),
    ]