# FROM python:3

# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# COPY . .

# RUN pip install -r requirements.txt

FROM python:3.8.0

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install libgl1-mesa-glx -y

# RUN apt-get gcc python3-dev musl-dev mariadb-connector-c-dev zlib-dev jpeg-dev
# RUN pip install mysqlclient
# requirements.txt에서 살핀 라이브러리를 설치하기 위해 필요한 gcc, musl-dev등을 미리 설치해 준다고 합니다
# ... 필요할지 모르겠지만 일단 넣었습니다.

COPY . /usr/src/app/

RUN pip install --default-timeout=100 future
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x ./videos/TwitchDownloaderCLI

RUN chmod +x ./videos/TwitchDownloader.sh
