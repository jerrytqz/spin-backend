# Generated by Django 4.0.4 on 2022-11-16 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spin', '0031_remove_user_items_found'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blacklistedjwt',
            options={'verbose_name': 'blacklisted JWT', 'verbose_name_plural': 'blacklisted JWTs'},
        ),
    ]
