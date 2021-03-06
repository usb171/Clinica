# Generated by Django 2.0.7 on 2019-06-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0014_auto_20190614_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='statusColor',
            field=models.CharField(blank=True, choices=[('#1079e9', 'AGENDADO'), ('#5a821c', 'CONFIRMADO'), ('#8B3A62', 'AGUARDANDO'), ('#00BFFF', 'EM ATENDIMENTO'), ('#32CD32', 'ATENDIDO')], default='AGENDADO', max_length=25, null=True, verbose_name='Status Cor'),
        ),
    ]
