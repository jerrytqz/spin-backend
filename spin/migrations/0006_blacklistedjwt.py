# Generated by Django 3.0.3 on 2020-08-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spin', '0005_remove_user_jwt_secret'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistedJWT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jwt', models.CharField(max_length=128)),
            ],
        ),
    ]
