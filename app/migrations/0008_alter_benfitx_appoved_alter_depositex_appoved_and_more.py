# Generated by Django 5.0.4 on 2024-10-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_account_swiftcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benfitx',
            name='appoved',
            field=models.CharField(blank=True, default='pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='depositex',
            name='appoved',
            field=models.CharField(blank=True, default='pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='appoved',
            field=models.CharField(blank=True, default='pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='appoved',
            field=models.CharField(blank=True, default='pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='appoved',
            field=models.CharField(blank=True, default='pending', max_length=50, null=True),
        ),
    ]