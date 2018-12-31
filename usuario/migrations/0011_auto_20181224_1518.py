# Generated by Django 2.0.7 on 2018-12-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_auto_20181223_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='admin',
            field=models.CharField(blank=True, choices=[('ON', 'ON'), ('OFF', 'OFF')], default='ON', max_length=25, null=True, verbose_name='Usuário Administrador ?'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='agendaPropria',
            field=models.CharField(blank=True, choices=[('ON', 'ON'), ('OFF', 'OFF')], default='ON', max_length=25, null=True, verbose_name='Usuário com Agenda Própria ?'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ativo',
            field=models.CharField(blank=True, choices=[('ON', 'ON'), ('OFF', 'OFF')], default='ON', max_length=25, null=True, verbose_name='Usuário Ativo ?'),
        ),
    ]