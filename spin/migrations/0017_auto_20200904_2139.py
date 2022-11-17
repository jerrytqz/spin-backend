# Generated by Django 3.0.3 on 2020-09-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spin', '0016_user_items_found'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
