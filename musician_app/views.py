from django.shortcuts import render, redirect
from . import forms
from . import models 
# Create your views here.
def musician(request):
    if request.method == "POST":
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("musician")
    else:
         musician_form = forms.MusicianForm()

    return render(request, "musician.html", {"form": musician_form})

def edit_musician(request,id):
    single_musician = models.Musician.objects.get(pk = id)
    musician_form = forms.MusicianForm(instance=single_musician)
    if request.method == "POST":
        musician_form = forms.MusicianForm(request.POST, instance=single_musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("home")
    # else:
    #      musician_form = forms.MusicianForm()

    return render(request, "musician.html", {"form": musician_form})
