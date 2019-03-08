# Generated by Django 2.0.7 on 2019-03-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190307_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='convenio',
            name='status',
            field=models.CharField(blank=True, choices=[('ON', 'ON'), ('OFF', 'OFF')], default='ON', max_length=4, null=True, verbose_name='Título Ativo ?'),
        ),
        migrations.AlterField(
            model_name='titulo',
            name='status',
            field=models.CharField(blank=True, choices=[('ON', 'ON'), ('OFF', 'OFF')], default='ON', max_length=4, null=True, verbose_name='Título Ativo ?'),
        ),
    ]
