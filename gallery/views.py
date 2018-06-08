from django.shortcuts import render
from .models import ArtWork
# Create your views here.
def home(request):
    artworks = ArtWork.objects
    return render(request, 'gallery/home.html',{'artworks':artworks})
