# Generated by Django 2.0.7 on 2018-12-26 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_usuario_funcionalidadeusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='enderecoCompleto',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='Endereço Completo'),
        ),
    ]
