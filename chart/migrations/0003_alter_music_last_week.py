# Generated by Django 3.2.6 on 2021-08-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_auto_20210806_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='last_week',
            field=models.CharField(max_length=100, null=True),
        ),
    ]