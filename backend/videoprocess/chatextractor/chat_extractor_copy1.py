# -*- coding: utf-8 -*-
import pandas as pd
from videoprocess.models import Video,Highlight

def extract_time(text):
    text=text.split("[")[1]
    text=text.split("]")[0]
    alltime=text.split("]")[0]
    time=alltime[:4]
    return time

# def extract_sec(text):
#     text=text.split("[")[1]
#     text=text.split("]")[0]
#     alltime=text.split("]")[0]
#     sec=alltime[5:7]
#     return sec

# def extract_name(text):
#     text=text.split("[")[1]
#     text=text.split("] ")[1]
#     name=text.split(": ")[0]
#     return name

def extract_text(text):
    text=text.split("[")[1]
    text=text.split("]")[1]
    text=text.split(": ")[1].split("\nName")[0]
    return text

# def extract_toptime(text):
#     text=text[:1]
#     return text

def selecthighlight(VIDEO_index):
    print("selecthighlight1")
    VIDEO_txt_PATH="/usr/src/app/videos/v"+str(VIDEO_index)+".txt"
    df = pd.read_table(VIDEO_txt_PATH) # 본인 경로!!
    print("selecthighlight2")
    df.columns=['origin']

    #print(df)

    df2= pd.DataFrame(columns = ['time', 'text'])

    #append까지 하려고 하니깐 len(df)는 너무 큰 가봐요..
    for i in range(len(df)) :
        df2=df2.append({'time':extract_time(str(df.iloc[i])), 'text':extract_text(str(df.iloc[i]))},ignore_index=True)
    print(df2)
    print("tailtest")
    print(df2.tail())
    
    highlight=pd.DataFrame(df2['time'].value_counts().head(5).rename_axis("TIME").reset_index(name="COUNTS"))
    print(highlight)
    print(highlight["TIME"].iloc[0])
    print(highlight["TIME"].iloc[1])
    print(type(highlight["TIME"].iloc[1]))
    for i in range(5):
        HIGHLIGHT_db_PATH="/usr/src/app/videos/v"+str(VIDEO_index)+"-h"+i+".mp4"
        new = Highlight(video_index = VIDEO_index, highlight_index = i, highlight_path = HIGHLIGHT_db_PATH, start=highlight["TIME"].iloc[i])  
        new.save()

def savetext():
    save1=open('./save_top1.txt','w',encoding='utf-8')
    save2=open('./save_top2.txt','w',encoding='utf-8')
    save3=open('./save_top3.txt','w',encoding='utf-8')
    save4=open('./save_top4.txt','w',encoding='utf-8')
    save5=open('./save_top5.txt','w',encoding='utf-8')

    for i in range(len(df)):
        if df2["time"].iloc[i]==(highlight["TIME"].iloc[0]):
            print(df2.iloc[i])
            save1.write(str(df2.iloc[i]))
    
        elif df2["time"].iloc[i]==(highlight["TIME"].iloc[1]):
            print(df2.iloc[i])
            save2.write(str(df2.iloc[i]))
        
        elif df2["time"].iloc[i]==(highlight["TIME"].iloc[2]):
            print(df2.iloc[i])
            save3.write(str(df2.iloc[i]))
    
        elif df2["time"].iloc[i]==(highlight["TIME"].iloc[3]):
            print(df2.iloc[i])
            save4.write(str(df2.iloc[i]))
    
        elif df2["time"].iloc[i]==(highlight["TIME"].iloc[4]):
            print(df2.iloc[i])
            save5.write(str(df2.iloc[i]))
