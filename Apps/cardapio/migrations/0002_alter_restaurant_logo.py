# Generated by Django 4.2.7 on 2023-11-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(upload_to='restaurant/', verbose_name='Logo'),
        ),
    ]
