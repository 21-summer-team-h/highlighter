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
from videoprocess.chatextractor.chat_extractor_copy1 import selecthighlight
@api_view(['POST'])
def download(request) :
    videoID = str(request.data.get('videoID'))      #vidoeID = 트위치영상 아이디
    if twitchDownload(videoID) == True :
        #selecthighlight(videoID)
        return Response(data="Downloaded")
    else :
        return Response(data="No video")

@api_view(['GET'])
def edit(request) :
    if True :
        return Response(status=status.HTTP_200_OK)
