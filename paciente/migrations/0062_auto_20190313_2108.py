# Generated by Django 2.0.7 on 2019-03-14 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0061_auto_20190313_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='grauParentesco',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='nomeFamiliar',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)'), ('VIUVO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]