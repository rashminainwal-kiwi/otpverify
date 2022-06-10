# Generated by Django 4.0.5 on 2022-06-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userdetails_last_login_alter_userdetails_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
