# Generated by Django 2.0.7 on 2019-06-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0019_auto_20190605_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='slug',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('VIUVO(A)', 'VIUVO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nomeCompleto',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, choices=[('FEMININO', 'FEMININO'), ('MASCULINO', 'MASCULINO')], default='MASCULINO', max_length=10, null=True, verbose_name='Sexo'),
        ),
    ]
