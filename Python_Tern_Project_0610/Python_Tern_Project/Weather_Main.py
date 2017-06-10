# -*- coding: utf-8 -*-

import requests
import re

class Weather():
    def __init__( self  ):
        self.url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108";
        self.recvd = requests.get(self.url);
        self.Coment = re.findall(r'<wf>(.+?)</wf' , self.recvd.text );
        self.Time = re.findall(r'<title>(.+?)</title>' , self.recvd.text );
        self.locations = re.findall(r'<location wl_ver="3">.+?</location>' , self.recvd.text , re.DOTALL);
        self.provinceList = ['서울ㆍ인천ㆍ경기도' ,'강원도영서' , '강원도영동' , '충청북도' , '대전ㆍ세종ㆍ충청남도' , '전라북도' , '광주ㆍ전라남도' , '대구ㆍ경상북도' , '부산ㆍ울산ㆍ경상남도'  , '제주도']
        self.cityDic = {'서울' : '서울ㆍ인천ㆍ경기도' , '인천' : '서울ㆍ인천ㆍ경기도' , '수원' : '서울ㆍ인천ㆍ경기도' , '파주' : '서울ㆍ인천ㆍ경기도' , '춘천' : '강원도영서' ,  '원주' :'강원도영서' ,'강릉' : '강원도영동' , '청주' : '충청북도' , '대전' : '대전ㆍ세종ㆍ충청남도' ,  '서산' : '대전ㆍ세종ㆍ충청남도' ,  '세종' : '대전ㆍ세종ㆍ충청남도' ,  '전주' : '전라북도' ,  '군산' : '전라북도' ,  '광주' : '광주ㆍ전라남도' , '목포' : '광주ㆍ전라남도' , '여수' : '광주ㆍ전라남도' , '대구' : '대구ㆍ경상북도' ,  '안동' : '대구ㆍ경상북도' , '포항' : '대구ㆍ경상북도' ,  '부산' : '부산ㆍ울산ㆍ경상남도' , '울산' : '부산ㆍ울산ㆍ경상남도' , '창원' : '부산ㆍ울산ㆍ경상남도' ,   '제주' : '제주도' , '서귀포' : '제주도'};
      
        #self.cityList = ['서울' , '수원' , '인천' ,  '파주' , '원주' , '춘천' , '강릉' , '청주' , '대전' , '서산' , '세종' , '군산' , '전주' , '목포' , '대구' , '광주' , '안동' , '여수' , '포항' , '부산' , '울산' , '창원' , '제주' , '서귀포'];
        self.Time = self.Time[1];
        self.ResultList = [];

        self.Parse_Info();

    def CommentString(self):
        self.Coment = re.findall(r'<wf>(.+?)</wf' , self.recvd.text );

        test = self.Coment[0].split('<![CDATA[');
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

    def Parse_Info(self):
        for loc in self.locations:
            prov = re.findall(r'<province>(.+)</province>' , loc);
            city = re.findall(r'<city>(.+)</city>' , loc);
    
            data = re.findall(r'<data>(.+?)</data>' , loc , re.DOTALL);
            for datum in data:
                #print(datum);#구름 정보

                mode = re.findall(r'<mode>(.+?)</mode>' , datum); 
                tmEf = re.findall(r'<tmEf>(.+?)</tmEf>' , datum); 
                wf = re.findall(r'<wf>(.+?)</wf>' , datum); 
                tmn = re.findall(r'<tmn>(.+?)</tmn>' , datum); 
                tmx = re.findall(r'<tmx>(.+?)</tmx>' , datum); 
                reli = re.findall(r'<reliability>(.+?)</reliability>' , datum);
                
                self.ResultList.append([prov[0] , city[0] , mode[0] , tmEf[0] , wf[0] ,  tmn[0] ,  tmx[0] , reli[0]]);
                row = '{},{},{},{},{},{},{},{}'.format(prov[0], city[0] , mode[0] , tmEf[0] , wf[0] , tmn[0] , tmx[0] , reli[0]);
                print(row);

       