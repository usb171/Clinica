# Generated by Django 2.0.7 on 2019-08-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190812_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlecampo',
            name='usuario_cpf',
            field=models.CharField(blank=True, choices=[('required', 'required'), ('no_required', 'no_required')], default='no_required', max_length=25, null=True, verbose_name='Usuário CPF'),
        ),
    ]
