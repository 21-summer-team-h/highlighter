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
    get_video_index = str(request.GET.get('video_index', '50'))
    path_to_file = '/usr/src/app/videos/vo' + get_video_index + '.mp4'
    f = open(path_to_file, 'rb')
    videoFile = File(f)
    response = HttpResponse(videoFile.read())
    response['Content-Disposition'] = 'attachment';
    return response

# 사용자가 입력한 clip 번호 받기
@api_view(['POST'])
def getNums(request) :
    clipNum = list(request.data.get('clipNum'))
    returnSelectCat = select_concatenate(clipNum)
    if returnSelectCat != 0 :
            return Response(data=returnSelectCat)
    else :
        return Response(data="Error")

# 모든 emotion list를 넘겨 주기
# 일단 3개를 모두 같은 list에 넣는 것으로 설정 
# 이렇게 되면 front에서 받아서 차례로 3개씩 출력해야 함
@api_view(['POST'])
def getAllEmotion(request) :
    print('get all emotion start')
    get_video_index = str(request.data.get('video_index'))
    django.db.close_old_connections()
    
    print('get_video_index' + get_video_index)
    all_emotion_list = list()
    for i in range(5):
        highlight_target = Highlight.objects.get(video_index = get_video_index, highlight_index = i)
        all_emotion_list.append(highlight_target.emotion_1)
        all_emotion_list.append(highlight_target.emotion_2)
        all_emotion_list.append(highlight_target.emotion_3)

    print('emotion_list : ' + str(all_emotion_list))
    return Response(data={
        "emotion_list": all_emotion_list
        })