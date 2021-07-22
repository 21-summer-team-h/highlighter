import subprocess
import os
from api.models import Video
from videoprocess.chatextractor.chat_extractor_copy1 import selecthighlight

import django.db

def twitchDownload(VIDEO_ID):
    # 현재 값이 아무것도 없으면 error 발생
    django.db.close_old_connections()
    target = Video.objects.order_by('-video_index')[0]

    VIDEO_index = int(target.video_index) + 1         #추가할 비디오 인덱스
    VIDEO_db_PATH="/usr/src/app/videos/v"+str(VIDEO_index)+".mp4"

    new = Video(video_index = VIDEO_index, video_path = VIDEO_db_PATH, highlight_count=5)  
    new.save()

    VIDEO_mp4_PATH="./videos/v"+str(VIDEO_index)+".mp4"
    VIDEO_txt_PATH="./videos/v"+str(VIDEO_index)+".txt"

    subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "--download-ffmpeg"])
    subprocess.run(["echo", "ffmpegcomplete"])
    remp4 = subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "-m", "VideoDownload", "--id", VIDEO_ID, "-o", VIDEO_mp4_PATH])
    subprocess.run(["echo", "mp4complete"])
    retxt = subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "-m", "ChatDownload", "--id", VIDEO_ID, "--timestamp-format", "Relative", "-o", VIDEO_txt_PATH])
    subprocess.run(["echo", "txtcomplete"])

    # highlight 수집
    django.db.close_old_connections()
    selecthighlight(VIDEO_index)

    if str(remp4.returncode) == '0' and  str(retxt.returncode) == '0':
        return VIDEO_index
    else:
        return 0
        