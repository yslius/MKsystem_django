# Generated by Django 3.2 on 2021-07-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKsystemApp', '0006_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(blank=True, default=0, null=True, verbose_name='')),
                ('date', models.DateTimeField(null=True, verbose_name='日時')),
            ],
        ),
    ]
