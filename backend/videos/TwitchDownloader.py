import subprocess
import os
from api.models import Video
from videoprocess.chatextractor.chat_extractor_copy1 import selecthighlight

import django.db

def twitchDownload(VIDEO_ID):
    try:
        django.db.close_old_connections()
        target = Video.objects.order_by('-video_index')[0]
        VIDEO_index = int(target.video_index) + 1         #추가할 비디오 인덱스
        
    except IndexError as error:
        VIDEO_index = 1
    VIDEO_db_PATH="/usr/src/app/videos/v"+str(VIDEO_index)+".mp4"
    django.db.close_old_connections()
    new = Video(video_index = VIDEO_index, video_path = VIDEO_db_PATH, highlight_count=5)  
    new.save()

    VIDEO_mp4_PATH="./videos/v"+str(VIDEO_index)+".mp4"
    VIDEO_txt_PATH="./videos/v"+str(VIDEO_index)+".txt"

    subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "--download-ffmpeg"])
    subprocess.run(["echo", "ffmpegcomplete"])
    remp4 = subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "-m", "VideoDownload", "--id", VIDEO_ID, "-o", VIDEO_mp4_PATH])
    
    if str(remp4.returncode) != '0':        #오류 발생 시 디비 삭제
        django.db.close_old_connections()
        delete_target = Video.objects.get(video_index = VIDEO_index)
        delete_target.delete()
        return 0
    retxt = subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "-m", "ChatDownload", "--id", VIDEO_ID, "--timestamp-format", "Relative", "-o", VIDEO_txt_PATH])
    
    if str(retxt.returncode) != '0':        #오류 발생 시 디비 삭제
        django.db.close_old_connections()
        delete_target = Video.objects.get(video_index = VIDEO_index)
        delete_target.delete()
        return 0
    # highlight 수집
    django.db.close_old_connections()
    selecthighlight(VIDEO_index)

    return VIDEO_index
        