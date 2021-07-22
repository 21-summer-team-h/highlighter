from pathlib import Path

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import django.db

from videos.TwitchDownloader import twitchDownload
import settings

from api.models import Video, Highlight

from django.core.files import File
from django.http import HttpResponse

@api_view(['POST'])
def download(request) :
    videoID = str(request.data.get('videoID'))      #videoID = 트위치영상 아이디
    returnTwitchDownload = twitchDownload(videoID)
    if returnTwitchDownload != 0 :
        return Response(data=returnTwitchDownload)
    else :
        return Response(data="No video")


@api_view(['GET'])
def edit(request) :
    if True :
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def getEmotion(request) :
    get_video_index = str(request.data.get('video_index'))
    django.db.close_old_connections()
    
    emotion_list = list()
    for i in range(5):
        highlight_target = Highlight.objects.get(video_index = get_video_index, highlight_index = i)
        emotion_list.append(highlight_target.emotion_1)

    return Response(data={
        "emotion_list": emotion_list
        })

@api_view(['GET'])
def getVideo(request) :
    get_video_index = str(request.data.get('video_index'))
    path_to_file = '/usr/src/app/videos/vo' + get_video_index + '.mp4'
    f = open(path_to_file, 'rb')
    videoFile = File(f)
    response = HttpResponse(videoFile.read())
    response['Content-Disposition'] = 'attachment';
    return response
