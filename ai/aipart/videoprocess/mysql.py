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
    cursor.execute(sql)
    db.close()

def insert_emotion(v_index, h_index, e1,e2,e3):
    db = pymysql.connect(
    user='awfawf',
    passwd='asfafw',
    host='awfawf',
    db='highlighter',
    charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "update highlightvideo set emotion_1 = "+e1+", emotion_2 = "+e2+", emotion_3 = "+e3+" where video_index = "+v_index+" and highlight_index="+h_index+";"
    cursor.execute(sql)
    db.close()