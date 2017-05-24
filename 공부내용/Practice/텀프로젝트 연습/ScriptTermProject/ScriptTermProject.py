# -*- coding: euc-kr -*-
# Form implementation generated from reading ui file 'StartWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore , QtGui , QtWidgets
from urllib.parse import quote
import urllib.request
import xml.etree.ElementTree as etree
from email.mime.base import MIMEBase



##미세먼지
numOfRows = '81'
pageSize = '10'
pageNo = '1'
startPage = '1'
dataTerm = 'DAILY'
sidoName = '대구'
sidoList = [' ', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
stationName = '정왕동'
action = ''
stateBT = 0

key = 'E56rYBX2d12Q1SjKzCO%2FtqvNtoJUFDPNoLnPKjV9J8hn5ay5E7J07oR5kuqp1NDq9YU5E9g8%2Bp3%2FlCbNYH6cHA%3D%3D'


url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
key, numOfRows, pageSize, pageNo, startPage, quote(sidoName))

data = urllib.request.urlopen(url).read()

#파일 저장
filename = "test.xml"
f = open(filename, "wb")
f.write(data)
f.close()

# 파싱하기
tree = etree.parse(filename)
root = tree.getroot()


################################################

###메일 정보 #####


host = "smtp.gmail.com" # Gmail STMP 서버 주소
port = "587";
senderAddr = "goflvhxj807@gmail.com" #보내는 사람 email 주소
recipientAddr = "dngur807@naver.com" # 받는 사람 email 주소

msg = MIMEBase("multipart" , "alternative");
msg['Subject'] = "미세먼지 및 자외선 정보 메일입니다."
msg['From'] = senderAddr;
msg['To'] = recipientAddr;
str1 , str2 , str3 , str4 , str5 = ' ' , ' ' , ' ' , ' ' , ' ';


class Ui_StartWindow(object):
    global sidoName , stationName , filename , data , url , tree , root;
    

    def retranslateUi(self, StartWindow):
        global action
        _translate = QtCore.QCoreApplication.translate;
        StartWindow.setWindowTitle(_translate("StartWindow", "MainWindow"))
        self.pushButton.setText(_translate("StartWindow", "미세먼지"))
        self.pushButton_2.setText(_translate("StartWindow", "자외선"))
        self.pushButton_3.setText(_translate("StartWindow", "메일 전송"))
        self.label_2.setText(_translate("StartWindow", "label 2"))



    def ClickFb(self):
        global stateBT;
        stateBT = 1;


        print("클릭 {0}" ,  stateBT);
        self.dustshow(self.stationcomboBox.currentIndex());
        #self.pushButton.hide();
        #self.label.setPixmap(QtGui.QPixmap("Resource/smallsmile1.png"))
        # self.dustshow(self.stationcomboBox.currentIndex())

    def dustshow(self , Indexnum):
        global stationName , root;
        _translate = QtCore.QCoreApplication.translate
        stationName = root[1][0][Indexnum][0].text
        for item in root.iter('item'):
            if item.findtext('stationName') == stationName:
                self.label_2.setText(_translate("StartWindow", item.findtext('stationName')))  # 초기값 정왕동

            
    def setupUI(self , StartWindow) :
        global stateBT;

        font = QtGui.QFont()
        font.setFamily("맑은 고딕");
        font.setPointSize(18)
        font.setBold(True);
        font.setWeight(20);

        
        StartWindow.setObjectName("StartWindow");
        StartWindow.resize(597 , 697) # 윈도우 사이즈 설정
        self.centralwidget = QtWidgets.QWidget(StartWindow);
        self.centralwidget.setObjectName("centralwidget");


        self.label = QtWidgets.QLabel(self.centralwidget);
        self.label.setGeometry(QtCore.QRect(0 , 0 , 600 , 700))
        self.label.setText("");
     #   self.label.setPixmap(QtGui.QPixmap("Resource/background.jpg"));
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget);        
        self.label_2.setGeometry(QtCore.QRect(225 , 109 , 105 , 51));
        self.label_2.setFont(font);
        self.label_2.setAlignment(QtCore.Qt.AlignCenter);#정렬
        self.label_2.setObjectName("label_3");
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget);
        self.pushButton.setGeometry(QtCore.QRect(30 , 30 , 161 , 71))
        self.pushButton.setFont(font);
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget);
        self.pushButton_2.setGeometry(QtCore.QRect(220 , 30 , 161 , 71 ))
        self.pushButton_2.setFont(font);
        self.pushButton_2.setObjectName("pushButton_2");


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget);
        self.pushButton_3.setGeometry(QtCore.QRect(410 , 30 , 161 , 71 ))
        self.pushButton_3.setFont(font);
        self.pushButton_3.setObjectName("pushButton_3");



        # 콤보 박스
        self.sidocomboBox = QtWidgets.QComboBox(self.centralwidget);
        self.sidocomboBox.setGeometry(QtCore.QRect(30 , 125 , 50 , 22))
        self.sidocomboBox.setObjectName("comboBox");

        for item in sidoList:
            self.sidocomboBox.addItem(item);
        



        self.stationcomboBox = QtWidgets.QComboBox(self.centralwidget);
        self.stationcomboBox.setGeometry(QtCore.QRect(80 , 125 ,90 ,22));
        self.stationcomboBox.setObjectName("comboBox2");
        self.stationcomboBox.addItem(' ')

        for item in root.iter('item'):
            self.stationcomboBox.addItem(item.findtext('stationName'));

    
        StartWindow.setCentralWidget(self.centralwidget) 

        self.retranslateUi( StartWindow)#버튼에 이름 설정
         # 버튼 연결하기
        self.pushButton.clicked.connect(self.ClickFb)
        
         #콤보박스를 통해서 시도를 선택했을 ㅤㄸㅒㅤ
        self.sidocomboBox.currentIndexChanged.connect(self.sido_select ,  self.sidocomboBox.currentIndex());
        

    def sido_select(self,Indexnum):
        print("변경 {0}" , Indexnum);
        global umOfRows, pageSize, pageNo, startPage, dataTerm, sidoName, sidoList, stationName, action, f, filename, tree, root, key, url, data, str3, str4;

        

        sidoName = sidoList[Indexnum]
        str1 = sidoList[Indexnum] # 시도 이름
        str2 = root[1][0][0][1].text # 현재 시간

        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
            key, numOfRows, pageSize, pageNo, startPage, quote(sidoName))

        data = urllib.request.urlopen(url).read();

          # 파일 저장
        filename = "test.xml"
        f = open(filename, "wb")
        f.write(data)
        f.close()

         # 파싱하기
        tree = etree.parse(filename)
        root = tree.getroot()

        self.stationcomboBox.clear()
        for item in root.iter('item'):
            self.stationcomboBox.addItem(item.findtext('stationName'))
        if stateBT == 2 :
            self.ultrashow(self.stationcomboBox.currentIndex())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUI(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())
