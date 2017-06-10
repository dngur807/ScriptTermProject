# -*- coding: utf-8 -*-

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import datetime
from xml.dom import minidom


urllib = urllib2;
WEATHER_KEY = "e800a2f0-d2bd-3ec0-afa3-1889b1612cfb";
#WEATHER_KEY = "b60cf560-bc58-3d04-8a79-a5993221d22d";

Wnow    = datetime.datetime.now();
Whour = Wnow.strftime('%H')

#content = 'weather';
#value = 'current';
#option = 'minutely';
  
if Whour >= "18" and Whour <= "4":
    time_h = "D"
else:
    time_h = "N"


def Parse_weather(content , value , option , sidoName , stationName) :
    print(sidoName + "   "  + stationName + " WeatherParse");

    params = {"version": "1", "city":"서울", "county":"강남구","village":"도곡동"} #딕셔너리 형식 - 사용하기 편리하다.
    headers = {"appKey": WEATHER_KEY};

    #r = urllib.Request.get_full_url("http://apis.skplanetx.com/weather/current/hourly" ,params=params, headers=headers);

    url = "http://apis.skplanetx.com/%s/%s/%s?version=1&lat=37.566826005485716&lon=126.9786567859313&city=%s&county=%s&village=%s&stnid=108" % (content, value, option , "경기", "의왕시", "오전동");
    req = urllib.Request(urllib.quote(url,'/:?=&'))
    req.add_header("appKey", WEATHER_KEY);
    responseRead = urllib.urlopen(req).read();
    end = responseRead.decode().replace("[","").replace("]","")

    fullPath = req.full_url + "&appKey=" + WEATHER_KEY;
    #파일 저장
    return end;

def getvalue_weather(dic , value):
    dic = json.loads(dic);
    dic = dic["weather"];
    dic = dic["minutely"];
    if value=="station":
        return dic["station"]
    elif value=="wind":
        return dic["wind"]
    elif value=="precipitation":
        return dic["precipitation"]
    elif value=="sky":
        return dic["sky"]
    elif value=="rain":
        return dic["rain"]
    elif value=="temperature":
        return dic["temperature"]
    elif value=="humidity":
        return dic["humidity"]
    elif value=="pressure":
        return dic["pressure"]
    elif value=="lightning":
        return dic["lightning"]
    elif value=="timeObservation":
        return dic["timeObservation"]
    else:
        return "정보없음"