from django.shortcuts import render
from .models import Video

def video_view(request):
    videos = Video.objects.filter(video_index=1)
    return render(request, 'index.html', {"videos": videos})