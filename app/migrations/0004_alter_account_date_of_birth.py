# Generated by Django 5.0.4 on 2024-10-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_account_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
