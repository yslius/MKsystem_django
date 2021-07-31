# Generated by Django 3.2 on 2021-06-08 06:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKsystemApp', '0017_alter_withdrawal_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10, verbose_name='ユーザID')),
                ('deposit_value', models.DecimalField(blank=True, decimal_places=8, default=0.0, max_digits=100, null=True, verbose_name='資産')),
                ('deposit_date', models.DateTimeField(null=True, verbose_name='変更日時')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='フォーマットが不正です。', regex='(^0\\d{9,10}$)|(^0\\d{2,3}-\\d{1,4}-\\d{4}$)')], verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='value',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.001), django.core.validators.RegexValidator(message='フォーマットが不正です。', regex='\\d{3}\\-?\\d{4}')], verbose_name=''),
        ),
    ]