# from TwitchDownloader import twitchDownload
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import settings
from videos.TwitchDownloader import twitchDownload
import subprocess
import os
from pathlib import Path

@api_view(['POST'])
def download(request) :
    videoID = str(request.data.get('videoID'))
    print(os.getcwd())
    if twitchDownload(videoID) == True :
        return Response(data="Downloaded")
    else :
        return Response(data="No video")

@api_view(['GET'])
def edit(request) :
    if True :
        return Response(status=status.HTTP_200_OK)


#def twitchDownload(VIDEO_ID='1078156676', VIDEO_NAME='test'):
    # 여길 수정해야 함. 이 파일의 위치로 수정해야할 듯.
    print(os.getcwd())
    #path = os.path.join(settings.FILES_DIR, 'TwitchDownloader.sh')
    #path = os.path.abspath("../videos/TwitchDownloader.sh")
    #path=os.path.join(settings.FILES_DIR, 'TwitchDownloader.sh')
    #return subprocess.call([path, VIDEO_ID, VIDEO_NAME])
