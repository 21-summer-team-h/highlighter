import subprocess
import os

def twitchDownload(VIDEO_ID='1078156676', VIDEO_NAME='test'):
    path = os.path.join("/usr/src/app/videos/TwitchDownloader.sh")
    sub= subprocess.call([path, VIDEO_ID,
                    VIDEO_NAME],shell=True)
    return sub