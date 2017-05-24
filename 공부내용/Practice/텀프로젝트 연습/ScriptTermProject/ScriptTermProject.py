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



##�̼�����
numOfRows = '81'
pageSize = '10'
pageNo = '1'
startPage = '1'
dataTerm = 'DAILY'
sidoName = '�뱸'
sidoList = [' ', '����', '�λ�', '�뱸', '��õ', '����', '����', '���', '���', '����', '���', '�泲', '����', '����', '���', '�泲', '����']
stationName = '���յ�'
action = ''
stateBT = 0

key = 'E56rYBX2d12Q1SjKzCO%2FtqvNtoJUFDPNoLnPKjV9J8hn5ay5E7J07oR5kuqp1NDq9YU5E9g8%2Bp3%2FlCbNYH6cHA%3D%3D'


url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
key, numOfRows, pageSize, pageNo, startPage, quote(sidoName))

data = urllib.request.urlopen(url).read()

#���� ����
filename = "test.xml"
f = open(filename, "wb")
f.write(data)
f.close()

# �Ľ��ϱ�
tree = etree.parse(filename)
root = tree.getroot()


################################################

###���� ���� #####


host = "smtp.gmail.com" # Gmail STMP ���� �ּ�
port = "587";
senderAddr = "goflvhxj807@gmail.com" #������ ��� email �ּ�
recipientAddr = "dngur807@naver.com" # �޴� ��� email �ּ�

msg = MIMEBase("multipart" , "alternative");
msg['Subject'] = "�̼����� �� �ڿܼ� ���� �����Դϴ�."
msg['From'] = senderAddr;
msg['To'] = recipientAddr;
str1 , str2 , str3 , str4 , str5 = ' ' , ' ' , ' ' , ' ' , ' ';


class Ui_StartWindow(object):
    global sidoName , stationName , filename , data , url , tree , root;
    

    def retranslateUi(self, StartWindow):
        global action
        _translate = QtCore.QCoreApplication.translate;
        StartWindow.setWindowTitle(_translate("StartWindow", "MainWindow"))
        self.pushButton.setText(_translate("StartWindow", "�̼�����"))
        self.pushButton_2.setText(_translate("StartWindow", "�ڿܼ�"))
        self.pushButton_3.setText(_translate("StartWindow", "���� ����"))
        self.label_2.setText(_translate("StartWindow", "label 2"))



    def ClickFb(self):
        global stateBT;
        stateBT = 1;


        print("Ŭ�� {0}" ,  stateBT);
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
                self.label_2.setText(_translate("StartWindow", item.findtext('stationName')))  # �ʱⰪ ���յ�

            
    def setupUI(self , StartWindow) :
        global stateBT;

        font = QtGui.QFont()
        font.setFamily("���� ���");
        font.setPointSize(18)
        font.setBold(True);
        font.setWeight(20);

        
        StartWindow.setObjectName("StartWindow");
        StartWindow.resize(597 , 697) # ������ ������ ����
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
        self.label_2.setAlignment(QtCore.Qt.AlignCenter);#����
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



        # �޺� �ڽ�
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

        self.retranslateUi( StartWindow)#��ư�� �̸� ����
         # ��ư �����ϱ�
        self.pushButton.clicked.connect(self.ClickFb)
        
         #�޺��ڽ��� ���ؼ� �õ��� �������� �Ԥ��¤�
        self.sidocomboBox.currentIndexChanged.connect(self.sido_select ,  self.sidocomboBox.currentIndex());
        

    def sido_select(self,Indexnum):
        print("���� {0}" , Indexnum);
        global umOfRows, pageSize, pageNo, startPage, dataTerm, sidoName, sidoList, stationName, action, f, filename, tree, root, key, url, data, str3, str4;

        

        sidoName = sidoList[Indexnum]
        str1 = sidoList[Indexnum] # �õ� �̸�
        str2 = root[1][0][0][1].text # ���� �ð�

        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
            key, numOfRows, pageSize, pageNo, startPage, quote(sidoName))

        data = urllib.request.urlopen(url).read();

          # ���� ����
        filename = "test.xml"
        f = open(filename, "wb")
        f.write(data)
        f.close()

         # �Ľ��ϱ�
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
