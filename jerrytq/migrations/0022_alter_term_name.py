# Generated by Django 4.0.4 on 2022-12-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jerrytq', '0021_term_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='name',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
