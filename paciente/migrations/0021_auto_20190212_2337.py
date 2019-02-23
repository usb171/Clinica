# Generated by Django 2.0.7 on 2019-02-13 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0020_auto_20190212_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('VIUVO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]
