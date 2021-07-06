#!/bin/bash

VIDEO_ID=$1
VIDEO_NAME=${2}.mp4
CHAT_NAME=${2}.mp4
VIDEO_PATH=/home/video

# 비디오, 채팅 내용 다운로드
# -> 다운로드가 완료됐음을 어떻게 알릴지?
# server.js에서 동기처리해서, 다운로드가 끝나야 다음 함수 수행하는 방향으로 진행하면 되나?
cd VIDEO_PATH || { echo "No such path. check /home/video exists"; exit 1; }

echo "> Video downloading start"
TwitchDownloaderCLI -m VideoDownload --id ${VIDEO_ID} -o ${VIDEO_NAME}
echo "> Video downloading end"

echo "> Chat downloading start"
TwitchDownloaderCLI -m ChatDownload --id ${VIDEO_ID} --timestamp-format Relative -o ${CHAT_NAME}
echo "> Chat downloading end"

exit 0
