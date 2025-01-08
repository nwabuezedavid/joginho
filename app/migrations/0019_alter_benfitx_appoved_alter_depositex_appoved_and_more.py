# Generated by Django 4.2.16 on 2024-10-14 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_intertransferx_accnum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benfitx',
            name='appoved',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('reversed', 'Reversed'), ('cancelled', 'Cancelled')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='depositex',
            name='appoved',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='depositex',
            name='method',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='accnum',
            field=models.CharField(blank=True, default=1020699495268, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='appoved',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('reversed', 'Reversed'), ('cancelled', 'Cancelled')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='swiftcode',
            field=models.CharField(blank=True, default='KKGIDJ1I', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='uuid',
            field=models.CharField(blank=True, default='2bf89e1d2f08', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='loanx',
            name='appoved',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('reversed', 'Reversed'), ('cancelled', 'Cancelled')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='accnum',
            field=models.CharField(blank=True, default=7361758717068, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='appoved',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('reversed', 'Reversed'), ('cancelled', 'Cancelled')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='uuid',
            field=models.CharField(blank=True, default='c8b122146', max_length=50, null=True),
        ),
    ]
