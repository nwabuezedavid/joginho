# Generated by Django 5.0.4 on 2024-10-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_loan_date_alter_localtransferx_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benfitx',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='depositex',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
