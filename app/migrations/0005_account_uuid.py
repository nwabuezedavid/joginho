# Generated by Django 5.0.4 on 2024-10-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_account_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='uuid',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
