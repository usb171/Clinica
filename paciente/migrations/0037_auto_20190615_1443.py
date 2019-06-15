# Generated by Django 2.0.7 on 2019-06-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0036_auto_20190614_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('SOLTEIRO(A)', 'VIUVO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('CASADO(A)', 'CASADO(A)'), ('VIUVO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]
