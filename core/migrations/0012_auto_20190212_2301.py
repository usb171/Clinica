# Generated by Django 2.0.7 on 2019-02-13 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190212_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinica',
            name='usuarioAdmin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]