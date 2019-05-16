# Generated by Django 2.0.7 on 2019-04-09 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_auto_20190408_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='grau1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Grau do Familiar 1'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='grau2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Grau do Familiar 2'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='grau3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Grau do Familiar 3'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='grau4',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Grau do Familiar 4'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nomeFamiliar1',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do Familiar 4'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nomeFamiliar2',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do Familiar 4'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nomeFamiliar3',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do Familiar 4'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nomeFamiliar4',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do Familiar 4'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, choices=[('FEMININO', 'FEMININO'), ('MASCULINO', 'MASCULINO')], default='MASCULINO', max_length=10, null=True, verbose_name='Sexo'),
        ),
    ]