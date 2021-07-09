#!/bin/bash

VIDEO_ID=$1
VIDEO_NAME=${2}.mp4
CHAT_NAME=${2}.txt
VIDEO_PATH=/app

# 비디오, 채팅 내용 다운로드
# -> 다운로드가 완료됐음을 어떻게 알릴지? -> 동기처리 혹은 메세지를 보내기 생각중
# server.js에서 동기처리한다 해도, sh만 실행시킨 다음 sh가 종료하기 전에 함수로 넘어갈 수도 있음.

# 해결 방안
# 노드는 동기 비동기
# 1. sh에서 다운로드가 끝난 후에, node에 메세지를 보내자.
# -> 리스트
# 2. 다운로드가 끝난 후에, 파일을 계속 확인하자.
# -> 파일 이름을 바꿔서 이용한다.
# 3. sh에서 binary file을 만들어서 node에 메세지를 보낸다.

# cd ${VIDEO_PATH}

echo "> ffmpeg downloading start"
./TwitchDownloaderCLI --download-ffmpeg
echo "> ffmpeg downloading end"

echo "> Video downloading start"
# ffmpeg가 없으면 다운로드를 못함.
./TwitchDownloaderCLI -m VideoDownload --id ${VIDEO_ID} -o ${VIDEO_NAME}
echo "> Video downloading end"

echo "> Chat downloading start"
./TwitchDownloaderCLI -m ChatDownload --id ${VIDEO_ID} --timestamp-format Relative -o ${CHAT_NAME}
echo "> Chat downloading end"

# curl을 이용하면, 다운로드 끝났다고 요청보낼 수 있음.
curl -X GET -H "Content-Type: application/json; charset=utf-8" -d "{'message': ${VIDEO_ID}}" http://127.0.0.1:3000/api/node/download

exit 0
