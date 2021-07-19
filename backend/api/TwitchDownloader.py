import subprocess


def twitchDownload(VIDEO_ID='1078156676', VIDEO_NAME='test'):
    return subprocess.run(["../videos/TwitchDownloader/TwitchDownloader.sh", VIDEO_ID,
                    VIDEO_NAME])