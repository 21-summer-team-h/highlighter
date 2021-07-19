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
    if twitchDownload(videoID) == True :
        return Response(data="Downloaded")
    else :
        return Response(data="No video")
    return Response(status=status.HTTP_201_OK)

@api_view(['GET'])
def edit(request) :
    if True :
        return Response(status=status.HTTP_200_OK)
