# Generated by Django 2.0.7 on 2018-12-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_auto_20181223_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='Email'),
        ),
    ]
