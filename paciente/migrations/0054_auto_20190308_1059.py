# Generated by Django 2.0.7 on 2019-03-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0053_auto_20190308_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]