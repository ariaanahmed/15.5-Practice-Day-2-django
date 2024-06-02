from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
    else:
        album_form = forms.AlbumForm
    return render(request, 'album.html', {'form': album_form})

def edit_album(request,id):
    single_album = models.Album.objects.get(pk = id)
    album_form = forms.AlbumForm(instance=single_album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=single_album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    # else:
    #     album_form = forms.AlbumForm

    return render(request, 'album.html', {'form': album_form})

def delete_album(request, id):
    single_album = models.Album.objects.get(pk = id)
    single_album.delete()
    return redirect('home')
