# Generated by Django 3.2.6 on 2021-08-06 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='artist_imgurl',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='artist_url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='cover_imgurl',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chart.music')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chart.music')),
            ],
        ),
    ]
