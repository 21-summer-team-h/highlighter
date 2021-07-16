import subprocess


def twitchDownload(VIDEO_ID='1078156676', VIDEO_NAME='test'):
    subprocess.run(["./TwitchDownloader.sh", VIDEO_ID,
                    VIDEO_NAME])
