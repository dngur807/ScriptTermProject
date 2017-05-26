# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
import UI_Main
import urllib.request
import xml.etree.ElementTree as etree
import http.cookiejar
from urllib.parse import quote
from xml.dom import minidom
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication, QMessageBox, QPushButton, QMainWindow

numOfRows = '81'
pageSize = '10'
pageNo = '1'
startPage = '1'
sidoName = '경기'
sidoList = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
stationName = '정왕동'

REG_KEY = 'E56rYBX2d12Q1SjKzCO%2FtqvNtoJUFDPNoLnPKjV9J8hn5ay5E7J07oR5kuqp1NDq9YU5E9g8%2Bp3%2FlCbNYH6cHA%3D%3D';
#url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
#key, numOfRows, pageSize, pageNo, startPage, quote(sidoName))


#data = urllib.request.urlopen(url).read()

##파일 저장
#filename = "test.xml"
#f = open(filename, "wb")
#f.write(data)
#f.close()

## 파싱하기
#tree = etree.parse(filename)
#root = tree.getroot()


SMTP_HOST = "smtp.gmail.com" # Gmail SMTP 서버 주소.
SMTP_PORT = "587"


class MainWindow(QDialog, UI_Main.UI_Image):
    def __init__( self , parent = None):
        super(MainWindow, self).__init__(parent)

        self.currentInfo = "";
        self.cj = http.cookiejar.CookieJar()
        #self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj));
        self._debug = True
        self.choiceNum = 0
        self._title = ""
        self._message = ""
        self._from_email = ""
        self._to_email = ""
        self._password = ""
        self._smtp_port = SMTP_PORT
        self._smtp_host = SMTP_HOST
        self._reg_key = REG_KEY
        self.numOfRows = numOfRows;
        self.pageSize = pageSize;
        self.pageNo = pageNo;
        self.startPage = startPage;
        self.sidoName = sidoName;
        self.sidoList = sidoList;
        self.stationName = stationName;
        

        self.ParseAirpollution();#파싱
        self.Setup(self);
        
        self.sidocomboBox.setCurrentIndex(-1);
        self.stationcomboBox.setCurrentIndex(-1);

        # 도시 선택 , 해당 인덱스 넘겨준다.
        self.sidocomboBox.currentIndexChanged.connect(self.Sido_Select , self.sidocomboBox.currentIndex());
        #self.stationcomboBox.currentIndexChanged.connect(self.Station_Select , self.stationcomboBox.currentIndex());        

        self.pushButton.clicked.connect(self.AirpollutionInfoShow);# 이름 검색 버튼 이벤트
        #버튼 이벤트 설정
        writeImageWidget(self.pic1,"/Resource/","pic1","png")
        self.pic1.setScaledContents(True)
        writeImageWidget(self.pic2,"/Resource/","pic2","png")
        self.pic2.setScaledContents(True)

# 버튼 클릭 지역 검색
    def ParseAirpollution(self):
        #if self.pushButton.clicked :
        #    nameSave = self.textEdit_7.toPlainText();#검색 후 입력 문자열 저장
        #    self.textBrowser_15.clear();# 글자 지우기
        print ( "Parse Start" );

        for sido in self.sidoList:
            url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
    self._reg_key, self.numOfRows, self.pageSize, self.pageNo, self.startPage, quote(sido))
            data = urllib.request.urlopen(url).read();
            #파일 저장
            filename = sido + ".xml"
            f = open(filename, "wb")
            f.write(data)
            f.close()
            print(filename + "저장 " );
        # 파싱하기
        self.tree = etree.parse(self.sidoName + '.xml');
        self.root = self.tree.getroot();

    def Sido_Select(self , Index) :
        self.sidoName = self.sidoList[Index];
        self.tree = etree.parse(self.sidoName + '.xml');
        self.root = self.tree.getroot();

        self.stationcomboBox.clear();
        for item in self.root.iter('item'):
            self.stationcomboBox.addItem(item.findtext('stationName'))
    def AirpollutionInfoShow(self):# 대기 오염 정보 출력 

        if ( self.stationcomboBox.currentIndex() == -1 or 
self.sidocomboBox.currentIndex() == -1) :
            return;

        #현재 시간 입력
        self.CurTimeLabel.setText(self._translate("CurTimeLabel" , self.root[1][0][0][1].text));
        



    

#def xmlParser(itemDomList):
#    itemList = []
#    for itemDom in itemDomList:
#        Item = {}
#        Item['IRDNT_CODE'] = GetTextFromItem(itemDom,'IRDNT_CODE') # 재료
#        Item['SUMRY'] = GetTextFromItem(itemDom,'SUMRY') # 설명
#        Item['CALORIE'] = GetTextFromItem(itemDom,'CALORIE') # 칼로리
#        Item['RECIPE_NM_KO'] = GetTextFromItem(itemDom,'RECIPE_NM_KO') # 요리 이름
#        Item['QNT'] = GetTextFromItem(itemDom,'QNT') # 권장 인원
#        Item['PC_NM'] = GetTextFromItem(itemDom,'PC_NM') # 가격
#        Item['TY_NM'] = GetTextFromItem(itemDom,'TY_NM') # 종류
#        Item['LEVEL_NM'] = GetTextFromItem(itemDom,'LEVEL_NM') # 난이도
#        Item['NATION_NM'] = GetTextFromItem(itemDom,'NATION_NM') # 국가
#        Item['RECIPE_ID'] = GetTextFromItem(itemDom,'RECIPE_ID') # 레시피 ID
#        Item['COOKING_TIME'] = GetTextFromItem(itemDom,'COOKING_TIME') # 요리 시간     
#        Item['IMG_URL'] = GetTextFromItem(itemDom,'IMG_URL') # 요리 사진
#        itemList.append(Item)
#    return itemList

def writeImageWidget(Widget, Address, File, Extension):
    # 레이블에 이미지를 넣어준다. 파일 주소, 파일명, 확장자 순으로 받아서 넣어준다.
    Widget.setPixmap(QPixmap('.' + str(Address) + str(File) + '.' + str(Extension)))
        

if __name__ == '__main__':
    app = QApplication(sys.argv);
    Mainfrom = MainWindow();
    Mainfrom.show();
    sys.exit(app.exec_());