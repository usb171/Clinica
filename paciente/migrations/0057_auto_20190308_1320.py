# Generated by Django 2.0.7 on 2019-03-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0056_auto_20190308_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('SOLTEIRO(A)', 'VIUVO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('CASADO(A)', 'CASADO(A)'), ('VIUVO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]
