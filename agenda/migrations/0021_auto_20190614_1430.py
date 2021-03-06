# Generated by Django 2.0.7 on 2019-06-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0020_auto_20190614_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='status',
            field=models.CharField(blank=True, choices=[('AGENDADO', 'AGENDADO'), ('CONFIRMADO', 'CONFIRMADO'), ('AGUARDANDO', 'AGUARDANDO'), ('EM ATENDIMENTO', 'EM ATENDIMENTO'), ('ATENDIDO', 'ATENDIDO'), ('NAO ATENDIMENTO', 'NAO ATENDIMENTO')], default='AGENDADO', max_length=25, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='statusColor',
            field=models.CharField(blank=True, choices=[('#1079e9', 'AGENDADO'), ('#5a821c', 'CONFIRMADO'), ('#8B3A62', 'AGUARDANDO'), ('#00BFFF', 'EM ATENDIMENTO'), ('#32CD32', 'ATENDIDO'), ('#30CD32', 'NAO ATENDIMENTO')], default='#1079e9', max_length=25, null=True, verbose_name='Status Cor'),
        ),
    ]
