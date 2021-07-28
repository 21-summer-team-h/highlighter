
from os import name
from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/download/', download, name="download_video_backend_2_twitch"),
    path('api/getVideo/', getVideo, name="download_video_twitch_2_backend"),
    path('api/getEmotion/', getEmotion, name="getEmotion_backend_2_frontend"),
    path('api/getAllEmotion/', getAllEmotion, name="getAllEmotion_backend_2_frontend"),
    path('api/getNums/', getNums, name="getNums_backend_2_frontend"),
    path('api/getClips/', getClips, name="getThumbnail_backend_2_frontend"),
    path('api/getMainImg/', getMainImg, name="get_main_image_backend_2_frontend")
]
