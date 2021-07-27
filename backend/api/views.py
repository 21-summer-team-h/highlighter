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

from django.http import HttpResponse, JsonResponse
from videoprocess.run import select_concatenate
import base64

import base64
import os
@api_view(['POST'])
def download(request) :
    videoID = str(request.data.get('videoID'))      #videoID = 트위치영상 아이디
    returnTwitchDownload = twitchDownload(videoID)
    if returnTwitchDownload != 0 :
        return Response(data=returnTwitchDownload)
    else :
        return Response(data="No video")


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
    response['Content-Disposition'] = 'attachment'
    return response

# 사용자가 입력한 clip 번호 받기
@api_view(['GET'])
def getNums(request) :
    clipNum = (request.GET.get('clipNum'))
    print("---" + str(clipNum))
    get_video_index = str(request.GET.get('video_index'))
    django.db.close_old_connections()
    returnSelectCat = select_concatenate(get_video_index, clipNum)
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

@api_view(['GET'])
def getClips(request) :
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
        encoded = base64.b64encode(imgFile.read())
        encoded = encoded.decode("UTF-8")

        temp_data={
            'thumbnail' : encoded,
            'emotionlist' : emotion_list
        }
        send_data.append(temp_data)
        if os.path.isfile(str(path_to_file)+".png"):        #썸네일 이미지 삭제
            os.remove(str(path_to_file)+".png")

    return JsonResponse(send_data, safe=False)
