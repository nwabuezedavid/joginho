# Generated by Django 4.2.16 on 2024-10-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_intertransferx_accnum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intertransferx',
            name='accnum',
            field=models.CharField(blank=True, default=5827417287565, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='swiftcode',
            field=models.CharField(blank=True, default='GVAZFZUH', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='uuid',
            field=models.CharField(blank=True, default='1c935bb1603a', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='accnum',
            field=models.CharField(blank=True, default=2349102404215, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='uuid',
            field=models.CharField(blank=True, default='29908dfff', max_length=50, null=True),
        ),
    ]
