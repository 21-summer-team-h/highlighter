from pathlib import Path

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from videos.thumbnail import create_thumbnail
import django.db

from videos.TwitchDownloader import twitchDownload
import settings

from api.models import Video, Highlight

from django.core.files import File
from django.http import HttpResponse , JsonResponse

import base64

@api_view(['POST'])
def download(request) :
    videoID = str(request.data.get('videoID'))      #videoID = 트위치영상 아이디
    returnTwitchDownload = 93#twitchDownload(videoID)
    if returnTwitchDownload != 0 :
        return Response(data=returnTwitchDownload)
    else :
        return Response(data="No video")


# @api_view(['GET'])
# def edit(request) :
#     if True :
#         return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def getEmotion(request) :
    print('get emotion start')
    get_video_index = str(request.data.get('video_index'))
    django.db.close_old_connections()
    
    print('get_video_index' + get_video_index)
    emotion_list = list()
    for i in range(5):
        highlight_target = Highlight.objects.get(video_index = get_video_index, highlight_index = i)
        emotion_list.append(highlight_target.emotion_1)

    print('emotion_list : ' + str(emotion_list))
    return Response(data={
        "emotion_list": emotion_list
        })

@api_view(['GET'])
def getVideo(request) :
    get_video_index = str(request.GET.get('video_index', '93'))
    path_to_file = '/usr/src/app/videos/vo' + get_video_index + '.mp4'
    f = open(path_to_file, 'rb')
    videoFile = File(f)
    response = HttpResponse(videoFile.read())
    response['Content-Disposition'] = 'attachment';
    return response

@api_view(['GET'])
def getThumbnail(request) :
    get_video_index = str(request.GET.get('video_index', '93'))
    send_data=[]
    for i in range(5):
        django.db.close_old_connections()
        highlight_target = Highlight.objects.get(video_index = get_video_index, highlight_index = i)
        emotion_list = list()
        emotion_list.append(highlight_target.emotion_1)
        emotion_list.append(highlight_target.emotion_2)
        emotion_list.append(highlight_target.emotion_3)
        path_to_file = '/usr/src/app/videos/v' + str(get_video_index) + '-h' + str(i)
        thumb=create_thumbnail(path_to_file)
        if thumb==0:                                #썸네일 제작에서 에러 발생시 빈 json파일 전송
            l={}
            return JsonResponse(l, safe=False)
        f = open(thumb, 'rb')
        imgFile = File(f)
        temp_data={
            'thumbnail' : str(base64.encodebytes(imgFile.read())),
            'emotionlist' : emotion_list
        }
        send_data.append(temp_data)
    
    return JsonResponse(send_data, safe=False)