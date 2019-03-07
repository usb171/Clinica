# Generated by Django 2.0.7 on 2019-02-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0034_auto_20190223_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('SOLTEIRO(A)', 'VIUVO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, choices=[('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO')], default='MASCULINO', max_length=10, null=True, verbose_name='Sexo'),
        ),
    ]
