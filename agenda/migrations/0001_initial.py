# Generated by Django 2.0.7 on 2019-05-16 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(blank=True, max_length=120, null=True, verbose_name='Título')),
                ('dataInicio', models.CharField(blank=True, max_length=120, null=True, verbose_name='Data Início')),
                ('dataFim', models.CharField(blank=True, max_length=120, null=True, verbose_name='Data Fim')),
                ('clinica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Clinica')),
            ],
        ),
    ]
