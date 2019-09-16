# Generated by Django 2.0.7 on 2019-06-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0016_auto_20190614_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='statusColor',
            field=models.CharField(blank=True, choices=[('#1079e9', 'AGENDADO'), ('#5a821c', 'CONFIRMADO'), ('#8B3A62', 'AGUARDANDO'), ('#00BFFF', 'EM ATENDIMENTO'), ('#32CD32', 'ATENDIDO')], default='AGENDADO', max_length=25, null=True, verbose_name='Status Cor'),
        ),
    ]