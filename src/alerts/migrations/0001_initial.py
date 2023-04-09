# Generated by Django 4.1 on 2022-08-28 08:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('json_data', models.CharField(blank=True, max_length=1000, null=True)),
                ('action_url', models.CharField(blank=True, max_length=500, null=True)),
                ('time', models.DateTimeField()),
                ('content', models.CharField(max_length=500, null=True)),
                ('summary', models.CharField(max_length=100)),
                ('severity', models.PositiveIntegerField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('alert_type', models.CharField(choices=[('Application', 'Application'), ('Action', 'Action'), ('Notification', 'Notification'), ('Marketing', 'Marketing')], default='Notification', max_length=20)),
            ],
        ),
    ]
