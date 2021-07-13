from django.shortcuts import render
from .models import Video

def video_view(request):
    videos = Video.objects.all()
    return render(request, 'index.html', {"videos": videos})