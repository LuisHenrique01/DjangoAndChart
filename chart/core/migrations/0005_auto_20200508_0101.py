# Generated by Django 3.0.5 on 2020-05-08 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200508_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casosporcidadepiaui',
            name='idIBGE',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='IBGE ID'),
        ),
    ]
