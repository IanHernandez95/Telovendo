# Generated by Django 4.0.4 on 2022-05-17 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTelovendo', '0007_categoria_alter_provedore_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedore',
            name='categoria',
            field=models.CharField(max_length=60),
        ),
    ]
