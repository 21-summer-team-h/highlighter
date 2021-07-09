FROM python
WORKDIR /dockertest
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
VOLUME /home/volume/video

# RUN pip install --trusted-host pypi.python.org -r requirements.txt 
CMD ["python3", "manage.py", "runserver", "0:8000"]
EXPOSE 8000
