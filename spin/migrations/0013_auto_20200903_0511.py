# Generated by Django 3.0.3 on 2020-09-03 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spin', '0012_auto_20200903_0504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventoryitem',
            options={'ordering': ['user', 'item']},
        ),
    ]
