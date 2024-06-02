from django.shortcuts import render
from musician_app.models import Musician
from album_app.models import Album

def home(request):
    album_data = Album.objects.all()
    musician_data = Musician.objects.all()
    
    combined_data = []
    counter = 1
    for musician in musician_data:
        for album in album_data:
            if album.musician_id == musician.id:
                combined_data.append({'counter': counter, 'musician': musician,'album': album,})
                counter += 1

    data = {
        'combined_data': combined_data,
    }
    return render(request, 'home.html', data)
