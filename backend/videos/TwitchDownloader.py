import subprocess
import os

def twitchDownload(VIDEO_ID):
    subprocess.run(["echo", VIDEO_ID])
    subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "--download-ffmpeg"])
    subprocess.run(["echo", "ffmpegcomplete"])
    remp4 = subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "-m", "VideoDownload", "--id", VIDEO_ID, "-o", "./videos/test.mp4"])
    subprocess.run(["echo", "mp4complete"])
    retxt = subprocess.run(["/usr/src/app/videos/TwitchDownloaderCLI", "-m", "ChatDownload", "--id", VIDEO_ID, "--timestamp-format", "Relative", "-o", "./videos/test.txt"])
    subprocess.run(["echo", "txtcomplete"])
    if str(remp4.returncode) == '0' and  str(retxt.returncode) == '0':
        return True
    else:
        return False