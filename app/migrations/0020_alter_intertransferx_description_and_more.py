# Generated by Django 4.2.16 on 2024-10-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_benfitx_appoved_alter_depositex_appoved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intertransferx',
            name='Description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='accnum',
            field=models.CharField(blank=True, default=2653128215807, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='swiftcode',
            field=models.CharField(blank=True, default='RUOTBKKZ', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='intertransferx',
            name='uuid',
            field=models.CharField(blank=True, default='05de8c813fbe', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='loanx',
            name='Description',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='accnum',
            field=models.CharField(blank=True, default=9796952338987, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='localtransferx',
            name='uuid',
            field=models.CharField(blank=True, default='8aa1e82eb', max_length=50, null=True),
        ),
    ]