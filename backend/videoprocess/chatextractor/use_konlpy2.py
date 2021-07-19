from konlpy.tag import Okt
from collections import Counter
import csv

filename = "./save_top4.txt" #가져올 채팅 파일
f = open(filename, 'r', encoding="utf-8")
news = f.read()

emoticon = ['']
# 일반적인 채팅 내용이 아닌 것들은 예외처리를 해주기 위해 리스트에 넣는다
# 근데 어차피 한글만 처리하는 거라서.. (konlpy)
# 이모티콘 이름은 다 영어라서 예외처리 할 필요 없을듯?

# 그리고 댓글 txt 파일 : [시간] [댓글내용] 만

#okt 객체 생성
okt = Okt()
noun = okt.nouns(news)
for i, v in enumerate(noun):
    if len(v) < 2: #한 글자 단어는 안쓰려고
        noun.pop(i)

count = Counter(noun)
f.close()

#명사 빈도 카운트
noun_list = count.most_common(3)    # 제일 많이 나온 명사 3개만 고르자
for v in noun_list:
    print(v)

# txt 파일에 저장
with open("save_chat1.txt", 'w', encoding='utf-8') as f:
    for v in noun_list:
            f.write(" ".join(map(str, v)))
            f.write("\n")
