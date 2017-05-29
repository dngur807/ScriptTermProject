# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
import UI_Main
import urllib
import urllib.request
import mysmtplib
import xml.etree.ElementTree as etree
import http.cookiejar
from urllib.parse import quote
from xml.dom import minidom
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
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

REG_KEY = 'qvrSOFP%2FQaIF3w89WIvoxu%2BvcrCYf5q1ln7n75YYhPVW3WZP99mM1jrseOHDjFuVqPm3FEsH5HhzYx0LWg1m2Q%3D%3D';

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

        self.Send_email_ID = ""
        self.Send_email_Psd = ""
        self.Recv_email_ID = ""
        self.TitleName = ""
        
        
       # self.ParseAirpollution();#파싱
        self.Setup(self);
        
        self.sidocomboBox.setCurrentIndex(-1);
        self.stationcomboBox.setCurrentIndex(-1);

        # 도시 선택 , 해당 인덱스 넘겨준다.
        self.sidocomboBox.currentIndexChanged.connect(self.Sido_Select , self.sidocomboBox.currentIndex());
        self.stationcomboBox.currentIndexChanged.connect(self.Station_Select , self.stationcomboBox.currentIndex());        

        self.pushButton.clicked.connect(self.AirpollutionInfoShow);# 이름 검색 버튼 이벤트
        self.SettingButton.clicked.connect(self.settingEmail);# 이메일 정보 셋팅
        self.dustSendButton.clicked.connect(self.DustsendEmail);#이메일 전송

        #버튼 이벤트 설정
        writeImageWidget(self.pic1,"/Resource/","pic1","png")
        self.pic1.setScaledContents(True)
        writeImageWidget(self.pic2,"/Resource/","pic2","png")
        self.pic2.setScaledContents(True)
        
        writeImageWidget(self.mainpic,"/Resource/","Main","png")
        self.mainpic.setScaledContents(True);
        
        writeImageWidget(self.mailBox_Img,"/Resource/","mail","jpg")
        self.mailBox_Img.setScaledContents(True);

# 버튼 클릭 지역 검색
    def ParseAirpollution(self , index):
        #if self.pushButton.clicked :
        #    nameSave = self.textEdit_7.toPlainText();#검색 후 입력 문자열 저장
        #    self.textBrowser_15.clear();# 글자 지우기
        print(sidoList[index] + "Parse");

        str1 = sidoList[index];
        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
        self._reg_key, self.numOfRows, self.pageSize, self.pageNo, self.startPage, quote(str1))
        data = urllib.request.urlopen(url).read();
        #파일 저장
        filename = "save.xml"
        f = open(filename, "wb")
        f.write(data)
        f.close()

        # 파싱하기
        self.tree = etree.parse(filename);
        self.root = self.tree.getroot();

    def Sido_Select(self , Index) :
        self.ParseAirpollution(Index);#파싱

        self.sidoName = self.sidoList[Index];
        self.tree = etree.parse('save.xml');
        self.root = self.tree.getroot();
       
        self.stationcomboBox.clear();
        for item in self.root.iter('item'):
            self.stationcomboBox.addItem(item.findtext('stationName'))

    def Station_Select(self , Index) :
        self.stationName = self.root[1][0][Index][0].text;

    def AirpollutionInfoShow(self):# 대기 오염 정보 출력 
        if ( self.stationcomboBox.currentIndex() == -1 or 
self.sidocomboBox.currentIndex() == -1) :
            return;
        #현재 시간 입력
        self.CurTimeLabel.setText(self._translate("CurTimeLabel" , self.root[1][0][0][1].text));
        for item in self.root.iter('item'):
            if item.findtext('stationName') == self.stationName:
                #정보 셋팅
                self.findustBrowser.setText(self._translate("findustBrowser", item.findtext('pm10Value') + " ㎍/㎥"));# 미세먼지
                self.OzoneBrowser.setText(self._translate("OzoneBrowser" , item.findtext('o3Value') )); # 오존 농도
                self.nitrogendioxideBrowser.setText(self._translate("nitrogendioxideBrowser" , item.findtext('no2Value') )); # 이산화 질소
                self.coValueBrowser.setText(self._translate("coValueBrowser" , item.findtext('coValue')));# 일산화 탄소
                self.so2GradeBrowser.setText(self._translate("so2GradeBrowser" , item.findtext('so2Grade')))# 아황산가스 지수
                self.coGradeBrowser.setText(self._translate("coGradeBrowser" , item.findtext('coGrade')))# 일산화탄소 지수
                self.o3GradeBrowser.setText(self._translate("o3GradeBrowser" , item.findtext('o3Grade')));# 오존 지수
                self.no2GradeBrowser.setText(self._translate("no2GradeBrowser" , item.findtext('no2Grade'))) # 이산화질소 지수
                self.khaiValueBrowser.setText(self._translate("khaiValueBrowser" , item.findtext('khaiValue'))); # 통합대기 수치
                
                
                if (item.findtext('pm10Value') != '-') :
                    ipm10Value = int(item.findtext('pm10Value'));
                    if ipm10Value >= 0 and ipm10Value <= 30:
                        writeImageWidget(self.Dustdisplay_img,"/Resource/","good2","png")
                        self.Dustdisplay_img.setScaledContents(True)

                        self.commentMsg = "여행가기 좋은 날입니다.\n실외활동 마음껏 하세요."

                    elif ipm10Value >= 31 and ipm10Value <= 80:
                        writeImageWidget(self.Dustdisplay_img,"/Resource/","good","png")
                        self.Dustdisplay_img.setScaledContents(True)
    
                        self.commentMsg = "실외활동하기에 무난한 날씨입니다..";

                    elif ipm10Value >= 81 and ipm10Value <= 150:
                        writeImageWidget(self.Dustdisplay_img,"/Resource/","bad1","png")
                        self.Dustdisplay_img.setScaledContents(True)

                        self.commentMsg = "왠만하면 실외활동은 자제하세요.\n마스크 착용 권장합니다."

                    elif ipm10Value >= 151:
                        writeImageWidget(self.Dustdisplay_img,"/Resource/","bad2","png")
                        self.Dustdisplay_img.setScaledContents(True)
                        self.commentMsg = "실내활동 하세요.\n마스크 필수 착용 권장합니다."
                    
                    self.CommentBrowser.setText(self._translate("CommentBrowser" , self.commentMsg));
                s = ""
                s += "====== <대기 오염 정보> =======\n<갱신 시간> :" + self.root[1][0][0][1].text  + "\n<시도> : " + sidoName + "\n<지역> :" + self.stationName + "\n<코멘트> :" + self.commentMsg + "\n\n<미세먼지 농도> :" +  item.findtext('pm10Value') + " ㎍/㎥\n" + "<오존 농도> : " + item.findtext('o3Value') + "\n<이산화 질소 농도> : " + item.findtext('no2Value') + "\n<일산화탄소 농도> :" + item.findtext('coValue') + "\n<아황산가스 지수> : " + item.findtext('so2Grade') + "\n<일산화탄소 지수> : " + item.findtext('coGrade') + "\n<오존 지수> : " + item.findtext('o3Grade') + "\n<이산화질소 지수> : " + item.findtext('no2Grade') + "\n<통합대기 수치> : " + item.findtext('khaiValue') 
                print(s);
                self.currentInfo = s;

    def settingEmail(self):
        if self.SettingButton.clicked :
            self.Send_email_ID = self.IDEdit.toPlainText(); # 아이디 셋팅
            self.Send_email_Psd = self.PasswordEdit.toPlainText();# 페스워드 설정
            self.Recv_email_ID =  self.SendToEdit.toPlainText();# 받는 Email ID
            self.TitleName = self.MailTitleEdit.toPlainText();
            self.SettingMsgBrowser.setText("메일 계정 세팅 완료");
    def DustsendEmail(self):#미세먼지
        #self.set
        if (self.Send_email_ID == "" or self.Send_email_Psd == ""
            or self.Recv_email_ID == ""):
            self.SendCheckBrowser.setText("메일 전송 실패");
            return None;

        msg = MIMEText(self.currentInfo, 'plain')
        msg['Subject'] = self.TitleName;
        msg['From'] = self.Send_email_ID;
        msg['To'] = self.Recv_email_ID;

        s = mysmtplib.MySMTP(self._smtp_host,self._smtp_port)
        s.ehlo()
        s.starttls()
        s.ehlo()
            
        try:
            s.login(self.Send_email_ID , self.Send_email_Psd) #로그인
        except Exception as e:
            self.__debug_print("Login Error! :" + str(e));
            return False;

        s.sendmail(self.Send_email_ID , [self.Recv_email_ID], msg.as_string())
        self.SendCheckBrowser.setText("메일 전송 완료");
        s.close();

        
def writeImageWidget(Widget, Address, File, Extension):
    # 레이블에 이미지를 넣어준다. 파일 주소, 파일명, 확장자 순으로 받아서 넣어준다.
    Widget.setPixmap(QPixmap('.' + str(Address) + str(File) + '.' + str(Extension)))
        

if __name__ == '__main__':
    app = QApplication(sys.argv);
    Mainfrom = MainWindow();
    Mainfrom.show();
    sys.exit(app.exec_());