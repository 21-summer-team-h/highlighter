import cv2
from moviepy.editor import *
from keras.preprocessing.image import img_to_array
from keras.models import load_model

from videoprocess.cut import cut_clip
from emotionprocess.FEC import FER
from videoprocess.concatenate import concatenate_clip, save_clip
import mysql


# cut
for i in range(1, highlight_max+1):
    exist_path = Video.objects.get(pk=i).video_path
    start = Address.objects.get(pk=i).start
    end = Address.objects.get(pk=i).end
    save_path = Address.objects.get(pk=i).highlight_path
    cut_clip(exist_path, start, end, save_path)
    mysql.cutvideo(8,i,save_path)   #video_index 8로 하이라이트번호를 1부터 highlight_max까지 각 경로를 저장



# get emotion
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface.xml')
emotion_classifier = load_model(r'./emotion_model.hdf5', compile=False)

for i in range(1, highlight_max+1):
    path = Address.objects.get(pk=i).highlight_path
    video = cv2.VideoCapture(path)
    emotion1, emotion2, emotion3 = FER(video, face_cascade)
    # pk=i인 객체의 emotion_1, emotion_2, emotion_3에 넣는 함수 추가하기
    mysql.update_emotion(8,i,emotion1,emotion2,emotion3)#video_index 8로 하이라이트번호를 1부터 highlight_max까지 각 감정을 추가


# concatenate
path_list = []

for i in range(1, highlight_max+1):
    path = Address.objects.get(pk=i).highlight_path
    path_list.append(path_list)
    concatenate = concatenate_clip(path_list)
mysql.update_concatenate(8, save_path) #video_index 8에 만들어진 비디오 경로 추가  
save_clip(save_path)

