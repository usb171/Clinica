# Generated by Django 2.0.7 on 2019-03-13 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0059_auto_20190309_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='grupoFamiliar',
            field=models.TextField(blank=True, null=True, verbose_name='Familiares'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('CASADO(A)', 'CASADO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]