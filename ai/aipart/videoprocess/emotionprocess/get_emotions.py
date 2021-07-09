import cv2
import numpy as np
from FEC import FER
from keras.preprocessing.image import img_to_array
from keras.models import load_model
# EMOTIONS = ["Angry","Disgusting","Fearful", "Happy", "Sad", "Surprising", "Neutral"]

# VIDEO_FILE_PATH = 
# video = cv2.VideoCapture(VIDEO_FILE_PATH)
# if video.isOpened() == False:
#   print("Failed to upload video!")
#   exit()

face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface.xml')
emotion_classifier = load_model(r'./emotion_model.hdf5', compile=False)

for i in range(1, highlight_max+1):
    path = Address.objects.get(pk=i).highlight_path
    video = cv2.VideoCapture(path)
    emotion1, emotion2, emotion3 = FER(video, face_cascade)
    # pk=i인 객체의 emotion_1, emotion_2, emotion_3에 넣는 함수 추가하기