# Generated by Django 2.0.7 on 2019-06-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0037_auto_20190615_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]
