import cv2
from moviepy.editor import *
from keras.preprocessing.image import img_to_array
from keras.models import load_model

from videoprocess.cut import cut_clip
from emotionprocess.FEC import FER
from videoprocess.concatenate import concatenate_clip, save_clip
import mysql

from .models import Video, Highlightvideo



# cut
for i in range(1, highlight_max+1):
    exist_path = Video.objects.get(pk=i).path
    # 자를 영상의 path를 불러옴
    start = Highlightvideo.objects.get(pk=i).start
    # 자를 영상의 시작 시간을 불러옴
    end = Highlightvideo.objects.get(pk=i).end
    # 자를 영상의 종류 시간을 불러옴
    save_path = Highlightvideo.objects.get(pk=i).highlight_path
    # 자르고 난 후 저장할 path를 불러옴
    cut_clip(exist_path, start, end, save_path)
    # 자르기 수행 + 저장 수행
    mysql.cutvideo(8,i,save_path)   #video_index 8로 하이라이트번호를 1부터 highlight_max까지 각 경로를 저장
    mysql.cutvideo(8, i, save_path) #video_index 8로 하이라이트저장

path_list = []
# 하이라이트 영상 path list

for i in range(1, highlight_max+1):
    path = Highlightvideo.objects.get(pk=i).highlight_path
    path_list.append(path)

# get emotion
face_cascade = cv2.CascadeClassifier(r'./emotionprocess/haarcascade_frontalface.xml')
emotion_classifier = load_model(r'./emotionprocess/emotion_model.hdf5', compile=False)

index = Highlightvideo.objects.get(pk=i).highlight_index



for path in range(path_list):
    video = cv2.VideoCapture(path)
    # path에서 비디오 추출
    emotion1, emotion2, emotion3 = FER(video, face_cascade)
    # 감정 분석 후 emotion1,2,3에다가 저장
    mysql.update_emotion(8,i,emotion1,emotion2,emotion3)
    #video_index 8로 하이라이트번호를 1부터 highlight_max까지 각 감정을 추가


# concatenate

for path in range(path_list):
    concatenate = concatenate_clip(path_list)

mysql.update_concatenate(8, save_path) 
# video_index 8에 만들어진 비디오 경로 추가  
save_clip(save_path)
# 저장

