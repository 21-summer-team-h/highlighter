from django.urls import path
from . import views

urlpatterns = [
    path('api/download/', views.download),
    path('api/getClips/', views.getClips),
    path('api/getNums/', views.getNums),
    path('api/getEmotion/', views.getEmotion),
    path('api/getVideo/', views.getVideo),
    path('api/getMainImg/', views.getMainImg)
]
