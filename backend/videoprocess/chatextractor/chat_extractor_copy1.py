# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import pandas as pd
from api.models import Video,Highlight
from videoprocess.run import video_process
def extract_time(text):
    text=text.split("[")[1]
    text=text.split("]")[0]
    alltime=text.split("]")[0]
    time=alltime[:4]
    return time
def extract_sec(text):
    text=text.split("[")[1]
    text=text.split("]")[0]
    alltime=text.split("]")[0]
    sec=alltime[5:7]
    return sec
def extract_text(text):
    text=text.split("[")[1]
    text=text.split("]")[1]
    text=text.split(": ")[1].split("\nName")[0]
    return text
def selecthighlight(VIDEO_index):
    VIDEO_txt_PATH="/usr/src/app/videos/v"+str(VIDEO_index)+".txt"
    df = pd.read_table(VIDEO_txt_PATH)
    df.columns=['origin']
    df2= pd.DataFrame(columns = ['time', 'text'])
    for i in range(len(df)) :
        sec=" "
        if int(extract_sec(str(df.iloc[i])))<10:
            sec=":00"
        elif int(extract_sec(str(df.iloc[i])))<20:
            sec=":10"
        elif int(extract_sec(str(df.iloc[i])))<30:
            sec=":20"
        elif int(extract_sec(str(df.iloc[i])))<40:
            sec=":30"
        elif int(extract_sec(str(df.iloc[i])))<50:
            sec=":40"
        else:
            sec=":50"
        df2=df2.append({'time': extract_time(str(df.iloc[i]))+sec, 'text':extract_text(str(df.iloc[i]))},ignore_index=True)
    highlight=pd.DataFrame(df2['time'].value_counts().head(5).rename_axis("TIME").reset_index(name="COUNTS"))
    highlight=highlight.sort_values(by=["TIME"], axis=0)
    for i in range(5):
        
        tmp = datetime.strptime(highlight["TIME"].iloc[i], '%H:%M:%S')
        HIGHLIGHT_db_PATH="/usr/src/app/videos/v"+str(VIDEO_index)+"-h"+str(i)+".mp4"
        # Video instance로 넣어줘야 하기 때문에 Video.objects.get이 필요함. (primary key라서)
        new = Highlight(video_index = Video.objects.get(video_index = VIDEO_index),
            highlight_index = i, highlight_path = HIGHLIGHT_db_PATH,
            start = str(tmp - timedelta(seconds=10))[11:], end = str(tmp + timedelta(seconds=10))[11:]
            )
        new.save()
                                                
    video_process(VIDEO_index)
def savetext():
    save1=open('./save_top1.txt','w',encoding='utf-8')
    save2=open('./save_top2.txt','w',encoding='utf-8')
    save3=open('./save_top3.txt','w',encoding='utf-8')
    save4=open('./save_top4.txt','w',encoding='utf-8')
    save5=open('./save_top5.txt','w',encoding='utf-8')
    for i in range(len(df)):
        if df2["time"].iloc[i]==(highlight["TIME"].iloc[0]):
            save1.write(str(df2.iloc[i]))
    
        elif df2["time"].iloc[i]==(highlight["TIME"].iloc[1]):
            save2.write(str(df2.iloc[i]))
        
        elif df2["time"].iloc[i]==(highlight["TIME"].iloc[2]):
            save3.write(str(df2.iloc[i]))
    
        elif df2["time"].iloc[i]==(highlight["TIME"].iloc[3]):
            save4.write(str(df2.iloc[i]))
    
        elif df2["time"].iloc[i]==(highlight["TIME"].iloc[4]):
            save5.write(str(df2.iloc[i]))