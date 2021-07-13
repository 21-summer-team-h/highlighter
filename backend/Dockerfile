# FROM python:3

# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# COPY . .

# RUN pip install -r requirements.txt

FROM python:3.8.0-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev
# requirements.txt에서 살핀 라이브러리를 설치하기 위해 필요한 gcc, musl-dev등을 미리 설치해 준다고 합니다
# ... 필요할지 모르겠지만 일단 넣었습니다.

COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt