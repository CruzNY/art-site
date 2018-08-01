from django.shortcuts import render
from .models import ArtWork
# Create your views here.
def home(request):
    artworks = ArtWork.objects
    return render(request, 'gallery/home.html',{'artworks':artworks})
def photo(request):
    return render(request, 'gallery/photography.html')
def sculp(request):
    return render(request, 'gallery/sculp.html')
def aboutMe(request):
    return render(request, 'gallery/aboutMe.html')
