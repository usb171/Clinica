# Generated by Django 2.0.7 on 2019-02-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0020_auto_20190213_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senhaPadraoAlterada',
            field=models.BooleanField(default=False),
        ),
    ]