from django.shortcuts import render, redirect, get_object_or_404
from .models import Music, Producer, Writer
import requests

# Create your views here.
def home(request):
    musics = Music.objects.all()
    query = request.GET.get('query')
    if query:
        musics = Music.objects.filter(title__icontains=query)
        return render(request, 'home.html', {'musics':musics, 'length':len(musics)})

    return render(request, 'home.html', {'musics':musics})

def detail(request, id): 
    music = get_object_or_404(Music, pk = id) 
    producers = Producer.objects.filter(number=id)
    writers = Writer.objects.filter(number=id)
    return render(request, 'detail.html', {'music': music,'producers':producers, 'writers':writers})

def init_db(request):
    url = "https://billboard2.p.rapidapi.com/hot_100"
    querystring = {"date":"2021-08-05"}
    headers = {
        'x-rapidapi-key': "337bab386fmshf0fcb4095596e1ep1bd2b7jsn5b64864e656b",
        'x-rapidapi-host': "billboard2.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=querystring)
    responses = res.json()
    for response in responses:
        new_music = Music()
        new_music.title = response['title'].replace('&#039;', "'")
        new_music.singer = response['artist_name']
        new_music.rank = response['rank']
        new_music.weeks_on_chart = response['history']['weeks_on_chart']
        new_music.last_week = response['history']['last_week']
        new_music.peak_date = response['history']['peak_date']
        new_music.peak_rank = response['history']['peak_rank']
        new_music.debut_date = response['history']['debut_date']
        new_music.debut_rank = response['history']['debut_rank']
        new_music.artist_url = 'https://www.billboard.com' + response['artist_url']
        try:
            new_music.artist_imgurl = 'https://charts-static.billboard.com' + response['artist_images']['sizes']['x-small-2x']['Name']
        except:
            new_music.artist_imgurl = "https://scontent-ssn1-1.xx.fbcdn.net/v/t1.6435-9/117591858_2956021041345448_8920210974041066255_n.jpg?_nc_cat=104&ccb=1-4&_nc_sid=730e14&_nc_ohc=LGy_GR22QT8AX_zN9mU&_nc_ht=scontent-ssn1-1.xx&oh=9141469a34783edd464bb2765494dbee&oe=61317778"
        try:
            new_music.cover_imgurl = 'https://charts-static.billboard.com' + response['title_images']['sizes']['medium']['Name']
        except:
            new_music.cover_imgurl = "https://scontent-ssn1-1.xx.fbcdn.net/v/t1.6435-9/117591858_2956021041345448_8920210974041066255_n.jpg?_nc_cat=104&ccb=1-4&_nc_sid=730e14&_nc_ohc=LGy_GR22QT8AX_zN9mU&_nc_ht=scontent-ssn1-1.xx&oh=9141469a34783edd464bb2765494dbee&oe=61317778"
        new_music.save()

        for producer in response['credited_producers']:
            new_producer = Producer()
            new_producer.number = new_music #new_music의 id가 들어감
            new_producer.name = producer['producer_short_name']
            new_producer.save()

        for writer in response['credited_writers']:
            new_writer = Writer()
            new_writer.number = new_music
            new_writer.name = writer['writer_short_name']
            new_writer.save()

    return redirect('home')
