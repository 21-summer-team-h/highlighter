import cv2
from moviepy.editor import *
from keras.preprocessing.image import img_to_array
from keras.models import load_model

from videoprocess.cut import cut_clip
from emotionprocess.FEC import FER
from videoprocess.concatenate import concatenate_clip, save_clip

from .models import Video, Highlight


def video_process():
    target = Video.objects.order_by('-video_index')[0]
    # 원본 영상 -> target
    target_number = target.video_index
    # target 영상의 video index
    target_count = target.highlight_count
    # target 영상이 가지고 있는 highlight의 갯수
    target_path = target.video_path
    # target 영상 경로

    for i in range(1, target_count+1):
        start = Highlight.objects.get(pk=target_number).start
        # 자를 영상의 시작 시간을 불러옴
        end = Highlight.objects.get(pk=i).end
        # 자를 영상의 종류 시간을 불러옴
        save_path = Highlight.objects.get(pk=i).highlight_path
        # 자르고 난 후 저장할 path를 불러옴

        """
        영상 저장 path
        다운로드 받은 비디오 : v$(video_index) ex)v5.mp4
        하이라이트 영상 : v$(video_index)-h$(highlight_index) ex)v5-h1.mp4
        완성된 영상 : vo$(video_index) ex) vo5.mp4
        """
    
        cut_clip(target_path, start, end, save_path)
        # 자르기 수행 + 저장 수행
    
        # mysql.cutvideo(8,i,save_path)   #video_index 8로 하이라이트번호를 1부터 highlight_max까지 각 경로를 저장
        # mysql.cutvideo(8, i, save_path) #video_index 8로 하이라이트저장

    path_list = []
    # 하이라이트 영상 path list

    # get emotion
    face_cascade = cv2.CascadeClassifier(r'./emotionprocess/haarcascade_frontalface.xml')
    emotion_classifier = load_model(r'./emotionprocess/emotion_model.hdf5', compile=False)



    for p in range(len(path_list)):
        video = cv2.VideoCapture(path_list[p])
        # path에서 비디오 추출
        emotion1, emotion2, emotion3 = FER(video, face_cascade)
        # 감정 분석 후 emotion1,2,3에다가 저장
        highlight_target = Highlight.objects.get(video_index = target_number)
        highlight_target = highlight.objects.get(highlight_index = p+1)
        highlight_target.emotion_1 = emotion1
        highlight_target.emotion_2 = emotion2
        highlight_target.emotion_3 = emotion3
        highlight_target.save()
        # mysql.update_emotion(8,i,emotion1,emotion2,emotion3)
        # #video_index 8로 하이라이트번호를 1부터 highlight_max까지 각 감정을 추가


    # concatenate

    for path in range(path_list):
        concatenate = concatenate_clip(path_list)

    highlight_target.path = save_path
    highlight_target.save()
    # mysql.update_concatenate(8, save_path) 
    # # video_index 8에 만들어진 비디오 경로 추가  
    save_clip(save_path)
    # 저장

