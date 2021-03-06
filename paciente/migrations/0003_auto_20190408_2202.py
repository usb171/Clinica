# Generated by Django 2.0.7 on 2019-04-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_auto_20190408_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='convenio1',
            field=models.CharField(blank=True, max_length=240, null=True, verbose_name='Convênio 1'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='convenio2',
            field=models.CharField(blank=True, max_length=240, null=True, verbose_name='Convênio 2'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='convenio3',
            field=models.CharField(blank=True, max_length=240, null=True, verbose_name='Convênio 3'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='convenio4',
            field=models.CharField(blank=True, max_length=240, null=True, verbose_name='Convênio 4'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='convenioValidade1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Validade do Convênio 1'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='convenioValidade2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Validade do Convênio 2'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='convenioValidade3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Validade do Convênio 3'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='convenioValidade4',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Validade do Convênio 4'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='numeroCarteira1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número Carteira 1'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='numeroCarteira2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número Carteira 2'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='numeroCarteira3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número Carteira 3'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='numeroCarteira4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número Carteira 4'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('VIUVO(A)', 'VIUVO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('DIVORCIADO(A)', 'DIVORCIADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]
