# Generated by Django 2.0.7 on 2019-01-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_auto_20190109_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='bairro',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='cep',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='cidade',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='complemento',
            field=models.TextField(blank=True, null=True, verbose_name='Complemento'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='convenios',
            field=models.TextField(blank=True, null=True, verbose_name='Convenios'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='estado',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='numero',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Número'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='observacao',
            field=models.TextField(blank=True, null=True, verbose_name='Observação'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='profissoes',
            field=models.TextField(blank=True, null=True, verbose_name='Profissões'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='quadra',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Quadra'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='rua',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Rua'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(blank=True, choices=[('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil'),
        ),
    ]
