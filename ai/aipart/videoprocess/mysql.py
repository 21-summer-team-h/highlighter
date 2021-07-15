import pymysql

def insert_cutvideo(v_index, h_index, h_path):
    db = pymysql.connect(
    user='asfasf',
    passwd='fafasf',
    host='awfawf',
    db='highlighter',
    charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "insert into highlightvideo(video_index, highlight_index, highlight_path) values("+v_index+","+h_index+","+h_path+");"
    #하이라이트 비디오 테이블에 하이라이트 비디오에 비디오 인덱스, 하이라이트 인덱스, 하이라이트 경로를 가지고 생성
    cursor.execute(sql)
    db.close()

def update_emotion(v_index, h_index, e1,e2,e3):
    db = pymysql.connect(
    user='awfawf',
    passwd='asfafw',
    host='awfawf',
    db='highlighter',
    charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "update highlightvideo set emotion_1 = "+e1+", emotion_2 = "+e2+", emotion_3 = "+e3+" where video_index = "+v_index+" and highlight_index="+h_index+";"
    #하이라이트비디오 테이블의 해당 하이라이트 비디오에 emotion들을 추가
    cursor.execute(sql)
    db.close()

def update_concatenate(v_index, concatenate_path):
    db = pymysql.connect(
    user='awfawf',
    passwd='asfafw',
    host='awfawf',
    db='highlighter',
    charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "update video set path = "+concatenate_path+" where video_index = "+v_index+";"
    #비디오 테이블의 해당 비디오부분의 경로에 완성된 비디오의 경로를 추가  (db수정되면 바꿔야됨)
    cursor.execute(sql)
    db.close()