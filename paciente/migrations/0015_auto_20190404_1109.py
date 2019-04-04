# Generated by Django 2.0.7 on 2019-04-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0014_auto_20190404_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('VIUVO(A)', 'VIUVO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, choices=[('FEMININO', 'FEMININO'), ('MASCULINO', 'MASCULINO')], default='MASCULINO', max_length=10, null=True, verbose_name='Sexo'),
        ),
    ]