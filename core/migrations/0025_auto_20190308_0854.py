# Generated by Django 2.0.7 on 2019-03-08 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20190308_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convenio',
            name='numeroCarteira',
        ),
        migrations.AlterUniqueTogether(
            name='convenio',
            unique_together={('nome', 'clinica')},
        ),
    ]