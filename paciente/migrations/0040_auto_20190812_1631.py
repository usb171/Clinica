# Generated by Django 2.0.7 on 2019-08-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0039_auto_20190812_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)'), ('VIUVO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, choices=[('FEMININO', 'FEMININO'), ('MASCULINO', 'MASCULINO')], default='MASCULINO', max_length=10, null=True, verbose_name='Sexo'),
        ),
    ]
