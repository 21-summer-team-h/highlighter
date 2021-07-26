import subprocess
import os
def create_thumbnail(path_to_file):
    print("create_thumbnail")
    s=subprocess.run(['/usr/src/app/ffmpeg', '-y', '-i', str(path_to_file)+'.mp4', '-ss', '00:00:10', '-vcodec', 'png', '-vframes', '1', str(path_to_file)+'.png'])
    # 해당 영상의 10초 부분의 이미지를 하나 가져와서 저장,-y : 이미 해당 이름으로 파일이 있을 경우 덮어쓰기 설정
    if s.returncode!=0:
        return 0
    print("thumbnaildown")
    return str(path_to_file)+'.png'