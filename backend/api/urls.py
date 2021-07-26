from django.urls import path
from . import views

urlpatterns = [
    path('api/download/', views.download),
    # path('api/edit/', views.edit),
    path('api/getClips/', views.getClips),
    path('api/getEmotion/', views.getEmotion),
    path('api/getVideo/', views.getVideo)
]
