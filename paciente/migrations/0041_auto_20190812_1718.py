# Generated by Django 2.0.7 on 2019-08-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0040_auto_20190812_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('SOLTEIRO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]