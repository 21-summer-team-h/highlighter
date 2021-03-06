"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
