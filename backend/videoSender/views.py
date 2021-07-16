from django.shortcuts import render

# Create your views here.
from django.core.files import File
from django.http import HttpResponse
from rest_framework.decorators import api_view
from backend.settings import BASE_DIR, MEDIA_ROOT

@api_view(['GET'])
def DownloadVideo(self):
    path_to_file = MEDIA_ROOT + '/sample-mp4-file.mp4'
    f = open(path_to_file, 'rb')
    videoFile = File(f)
    response = HttpResponse(videoFile.read())
    response['Content-Disposition'] = 'attachment';
    return response