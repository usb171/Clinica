# Generated by Django 2.0.7 on 2019-02-13 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0016_auto_20190212_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('SOLTEIRO(A)', 'VIUVO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('CASADO(A)', 'CASADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]
