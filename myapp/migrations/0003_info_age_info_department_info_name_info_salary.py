# Generated by Django 4.1.7 on 2023-08-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_info_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='department',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
