from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=200)
    singer = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    weeks_on_chart = models.CharField(max_length=100)
    last_week = models.CharField(max_length=100, null=True)
    peak_date = models.CharField(max_length=100)
    peak_rank = models.CharField(max_length=10)
    debut_date = models.CharField(max_length=100)
    debut_rank = models.CharField(max_length=10)
    artist_url = models.CharField(max_length=500, null=True)
    artist_imgurl = models.CharField(max_length=500, null=True)
    cover_imgurl = models.CharField(max_length=500, null=True)

class Producer(models.Model):
    number = models.ForeignKey(Music, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
class Writer(models.Model):
    number = models.ForeignKey(Music, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)