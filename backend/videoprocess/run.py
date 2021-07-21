import cv2
from moviepy.editor import *
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

from videoprocess.videoprocess.cut import cut_clip
from videoprocess.emotionprocess.FEC import FER
from videoprocess.videoprocess.concatenate import concatenate_clip

from api.models import Video, Highlight

    #vo5.mp4
def all_concatenate(target,path_list):
    # concatenate
    final_path=target.final_path
    concatenate_clip(final_path,path_list)

    # mysql.update_concatenate(8, save_path) 
    # # video_index 8에 만들어진 비디오 경로 추가  

def get_emotion(target,path_list):
    # get emotion
    face_cascade = cv2.CascadeClassifier('/usr/src/app/videoprocess/emotionprocess/haarcascade_frontalface.xml')
    emotion_classifier = load_model('/usr/src/app/videoprocess/emotionprocess/emotion_model.hdf5', compile=False)

    for p in range(len(path_list)):
        print("감정시작")
        video = cv2.VideoCapture(path_list[p])
        # path에서 비디오 추출
        emotion1, emotion2, emotion3 = FER(video, face_cascade, emotion_classifier)
        # 감정 분석 후 emotion1,2,3에다가 저장
        print("asdasd")
        highlight_target = Highlight.objects.get(video_index = target.video_index, highlight_index = p)
        highlight_target.update(emotion_1 = emotion1)
        highlight_target.update(emotion_2 = emotion2)
        highlight_target.update(emotion_3 = emotion3)
        print("감정중"+str(p)+"")
        # mysql.update_emotion(8,i,emotion1,emotion2,emotion3)
        # #video_index 8로 하이라이트번호를 1부터 highlight_max까지 각 감정을 추가
    #all_concatenate(target,path_list)

def video_process():
    target = Video.objects.order_by('-video_index')[0]
    print("-----")
    # 원본 영상 -> target
    target_number = target.video_index
    print(target_number)
    # target 영상의 video index
    target_count = target.highlight_count
    print(target_count)
    print(type(target_count))
    # target 영상이 가지고 있는 highlight의 갯수
    target_path = target.video_path
    # target 영상 경로

    print("hi")

    path_list = []
    # 하이라이트 영상 path list

    for i in Highlight.objects.filter(video_index=target_number):
        print("l")
        
        print("get video : " + str(i))

        start = i.start
        # 자를 영상의 시작 시간을 불러옴
        print("start:" + str(start))
        end = i.end
        # 자를 영상의 종류 시간을 불러옴
        save_path = i.highlight_path
        # 자르고 난 후 저장할 path를 불러옴
        path_list.append(save_path)

        print("ㅎㅎㅎ")
        """
        영상 저장 path
        다운로드 받은 비디오 : v$(video_index) ex)v5.mp4
        하이라이트 영상 : v$(video_index)-h$(highlight_index) ex)v5-h1.mp4
        완성된 영상 : vo$(video_index) ex) vo5.mp4
        """
        print(start)
        print(type(start))
        print(end)
        print(type(end))
        print("starttime")
        print(str(start))
        starttime=(int(str(start)[0:2])*3600 + int(str(start)[3:5])*60 + int(str(start)[6:8]))
        print(starttime)
        endtime=(int(str(end)[0:2])*3600 + int(str(end)[3:5])*60 + int(str(end)[6:8]))
        print(endtime)
        print(path_list)

        cut_clip(target_path, starttime, endtime, save_path)
        # 자르기 수행 + 저장 수행

    print("여기???")
    print(path_list)

    get_emotion(target,path_list)
video_process()