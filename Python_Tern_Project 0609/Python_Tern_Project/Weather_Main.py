# -*- coding: utf-8 -*-

import requests
import re
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108";
recvd = requests.get(url);


Coment = re.findall(r'<wf>(.+?)</wf' , recvd.text );
locations = re.findall(r'<location wl_ver="3">.+?</location>' , recvd.text , re.DOTALL);# ?? ?ȿ? ???? ?????̼? ã???ش?,.


provinceList = ['서울ㆍ인천ㆍ경기도' ,'강원도영서' , '강원도영동' , '충청북도' , '대전ㆍ세종ㆍ충청남도' , '전라북도' , '광주ㆍ전라남도' , '대구ㆍ경상북도' , '부산ㆍ울산ㆍ경상남도'  , '제주도']
cityList = ['서울' , '인천' , '수원' , '파주' , '춘천' , '원주' , '강릉' , '청주' , '대전' , '서산' , '세종' , '전주' , '군산' , '광주' , '목포' , '여수' ,'대구' , '안동' , '포항' , '부산' ,'울산' ,'창원' ,  '제주' , '서귀포'];

def CommentString(recvd):
    Coment = re.findall(r'<wf>(.+?)</wf' , recvd.text );

    test = Coment[0].split('<![CDATA[');
    for i in range( len(test)):
        if '' == test[i]:
            del test[i];
            break;
    str = "";
    for i in test:
        str += i ; 

    test = str.split('<br />');
    str = "";
    for i in test:
       str += i ; 
    test = str.split(']]>');

    str = "";
    for i in test:
       str += i ; 

    return str;

    
for loc in locations:
    prov = re.findall(r'<province>(.+)</province>' , loc);
    city = re.findall(r'<city>(.+)</city>' , loc);
    
    data = re.findall(r'<data>(.+?)</data>' , loc , re.DOTALL);
    for datum in data:
        #print(datum);#구름 정보

        # 문제
        # mode를 비롯한 나머지를 찾아보세요   
        mode = re.findall(r'<mode>(.+?)</mode>' , datum); 
        tmEf = re.findall(r'<tmEf>(.+?)</tmEf>' , datum); 
        wf = re.findall(r'<wf>(.+?)</wf>' , datum); 
        tmn = re.findall(r'<tmn>(.+?)</tmn>' , datum); 
        tmx = re.findall(r'<tmx>(.+?)</tmx>' , datum); 
        reli = re.findall(r'<reliability>(.+?)</reliability>' , datum);
       # print(prov[0] , city[0] , mode[0] , tmEf[0] , wf[0] , tmn[0] , tmx[0] , reli[0]);
    
        row = '{},{},{},{},{},{},{},{}'.format(prov[0] , "    ", city[0] , mode[0] , tmEf[0] , wf[0] , tmn[0] , tmx[0] , reli[0]);
        print(row);


       