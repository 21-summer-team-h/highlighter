from django.shortcuts import render

# Create your views here.
from django.core.files import File
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def DownloadVideo(request):
    path_to_file = request.data.get('outputPath')
    f = open(path_to_file, 'rb')
    videoFile = File(f)
    response = HttpResponse(videoFile.read())
    response['Content-Disposition'] = 'attachment';
    return response