# Generated by Django 3.1.1 on 2020-09-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200925_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='on_which_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='time_taken',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
