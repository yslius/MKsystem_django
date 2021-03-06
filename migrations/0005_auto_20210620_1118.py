# Generated by Django 3.2 on 2021-06-20 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKsystemApp', '0004_asset_stop_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='operate_user_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='操作したユーザID'),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='operate_user_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='操作したユーザID'),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='status',
            field=models.CharField(blank=True, default='処理中', max_length=10, null=True, verbose_name='状況'),
        ),
    ]
