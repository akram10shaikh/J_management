# Generated by Django 4.1.7 on 2023-08-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_info_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
    ]