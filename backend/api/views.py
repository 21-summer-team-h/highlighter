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
    videoID = str(request.data.get('videoID'))      #vidoeID = 트위치영상 아이디
    returnTwichDownload = twitchDownload(videoID)
    if returnTwichDownload != 0 :
        return Response(data=returnTwichDownload)
    else :
        return Response(data="No video")

@api_view(['GET'])
def edit(request) :
    if True :
        return Response(status=status.HTTP_200_OK)
