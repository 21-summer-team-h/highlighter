FROM python

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

# 실행될 python 파일 이름
# CMD ["app.py"]