# Generated by Django 2.0.7 on 2019-03-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0021_usuario_senhapadraoalterada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='titulo',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Título'),
        ),
    ]
