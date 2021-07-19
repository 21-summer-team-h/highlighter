# from TwitchDownloader import twitchDownload
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import subprocess
import os
from pathlib import Path

@api_view(['POST'])
def download(request) :
    videoID = str(request.data.get('videoID'))
    
    if twitchDownload(videoID) == True :
        return Response(data="Downloaded")
    else :
        return Response(data="No video")

@api_view(['GET'])
def edit(request) :
    if True :
        return Response(status=status.HTTP_200_OK)


def twitchDownload(VIDEO_ID='1078156676', VIDEO_NAME='test'):
    # 여길 수정해야 함. 이 파일의 위치로 수정해야할 듯.
    path = os.path.join("../videos/TwitchDownloader.sh")
    return subprocess.run([path, VIDEO_ID, VIDEO_NAME])