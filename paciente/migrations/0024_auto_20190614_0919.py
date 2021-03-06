# Generated by Django 2.0.7 on 2019-06-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0023_auto_20190614_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('VIUVO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, choices=[('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO')], default='MASCULINO', max_length=10, null=True, verbose_name='Sexo'),
        ),
    ]
