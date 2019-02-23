# Generated by Django 2.0.7 on 2019-02-13 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190212_2301'),
        ('usuario', '0017_auto_20190212_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='clinicas',
            field=models.ManyToManyField(blank=True, to='core.Clinica'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='clinicaAtual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clinicaAtual', to='core.Clinica'),
        ),
    ]
