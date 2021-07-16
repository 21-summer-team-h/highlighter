from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.twitchDownload import twitchDownload

@api_view(['POST'])
def download(request) :
    videoID = request.data.get('videoID')
    
    if twitchDownload(videoID) == True :
        return Response(data="Downloaded")
    else :
        return Response(data="No video")

@api_view(['GET'])
def edit(request) :
    if True :
        return Response(status=status.HTTP_200_OK)
