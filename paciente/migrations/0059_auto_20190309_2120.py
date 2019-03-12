# Generated by Django 2.0.7 on 2019-03-10 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0058_auto_20190308_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='idade',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Idade'),
        ),
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