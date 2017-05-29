# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore , QtGui , QtWidgets
import UI_Utility

class UI_Image(object):
    def Setup(self , Dialog):
      
        Dialog.setObjectName("Dialog");
        Dialog.resize(704 , 826);
    
        font = QtGui.QFont();
        font.setFamily("휴먼매직체");
        self.tabWidget = UI_Utility.Create_TabWidget(Dialog , "tabWidget" , QtCore.QRect(20 , 160 , 661 , 631) , font);

        self.tab1 = UI_Utility.Create_Widget("tab1");
        
        font = UI_Utility.Create_Font(setFamily = "휴먼매직체" , setWeight = 75 , setBold = True);
  
        self.pushButton = UI_Utility.Create_PushButton("pushButton" , self.tab1 , QtCore.QRect(280 , 80 , 93 , 28 ) ,font );# 찾기 버튼

        self.sidocomboBox = UI_Utility.Create_ComboBox("sidocomboBox" , self.tab1 , QtCore.QRect(250 , 50, 50 , 20));
        #아이템 서울 경기 ,,,,
        for item in self.sidoList:
            self.sidocomboBox.addItem(item)
        
        self.stationcomboBox = UI_Utility.Create_ComboBox("stationcomboBox" , self.tab1 , QtCore.QRect(250 + 50 , 50 , 70 , 20));
        #for item in self.root.iter('item'):
        #    self.stationcomboBox.addItem(item.findtext('stationName'))

        #시간 출력
        font = UI_Utility.Create_Font(setFamily = "휴먼매직체" , setWeight = 75  , setBold = True , setPointSize = 18 , setItalic = False , setUnderline = False);
        self.CurTimeLabel = UI_Utility.Create_Label("CurTimeLabel" , self.tab1 ,  QtCore.QRect(230 , 130, 550 , 20) , font);


        #미세먼지 농도
        font = UI_Utility.Create_Font(setFamily = "휴먼매직체" , setWeight = 75  , setBold = True , setPointSize = 11);
        self.findustlabel = UI_Utility.Create_Label("findustlabel" , self.tab1 , QtCore.QRect(270, 195, 81, 21) , font)
        self.findustBrowser = UI_Utility.Create_TextBrowser("findustBrowser" , self.tab1 , QtCore.QRect(360, 190, 211, 31));

        # 오존 농도
        self.Ozonelabel = UI_Utility.Create_Label("Ozonelabel" , self.tab1 , QtCore.QRect(300, 235, 81, 21) , font)
        self.OzoneBrowser = UI_Utility.Create_TextBrowser("OzoneBrowser" , self.tab1 , QtCore.QRect(360, 190 + 40 , 211, 31));
        
        # 이산화질소 농도
        self.nitrogendioxidelable = UI_Utility.Create_Label("nitrogendioxidelable" , self.tab1 , QtCore.QRect(260, 235 + 40, 95, 21) , font)
        self.nitrogendioxideBrowser = UI_Utility.Create_TextBrowser("nitrogendioxideBrowser" , self.tab1 , QtCore.QRect(360, 190 + 40* 2 , 211, 31));

        # 일산화탄소 농도coValue
        self.coValuelable = UI_Utility.Create_Label("coValuelable" , self.tab1 , QtCore.QRect(260, 235 + 40 * 2, 95, 21) , font)
        self.coValueBrowser = UI_Utility.Create_TextBrowser("coValueBrowser" , self.tab1 , QtCore.QRect(360, 190 + 40 * 3 , 211, 31));
        
        # 아황산가스 지수
        self.so2Gradelable = UI_Utility.Create_Label("so2Gradelable" , self.tab1 , QtCore.QRect(258, 235 + 40 * 3, 97, 21) , font)
        self.so2GradeBrowser = UI_Utility.Create_TextBrowser("so2GradeBrowser" , self.tab1 , QtCore.QRect(360, 190 + 40 * 4 , 211, 31));
        
        #일산화 탄소 지수 
        self.coGradelabel = UI_Utility.Create_Label("coGradelabel" , self.tab1 , QtCore.QRect(258, 235 + 40 * 4, 97, 21) , font)
        self.coGradeBrowser = UI_Utility.Create_TextBrowser("coGradeBrowser" , self.tab1 , QtCore.QRect(360, 190 + 40 * 5 , 211, 31));

        #오존 지수 지수 
        self.o3Gradelabel = UI_Utility.Create_Label("o3Gradelabel" , self.tab1 , QtCore.QRect(300, 235 + 40 * 5, 81, 21) , font)
        self.o3GradeBrowser = UI_Utility.Create_TextBrowser("o3GradeBrowser" , self.tab1 , QtCore.QRect(360, 190 + 40 * 6 , 211, 31));

        # 이산화질소 지수
        self.no2Gradelable = UI_Utility.Create_Label("no2Gradelable" , self.tab1 , QtCore.QRect(258 ,  235 + 40 * 6, 97, 21) , font);
        self.no2GradeBrowser = UI_Utility.Create_TextBrowser("no2GradeBrowser" , self.tab1 , QtCore.QRect(360, 190 + 40 * 7 , 211, 31));

        # 통합대기 수치
        self.khaiValuelable = UI_Utility.Create_Label("khaiValuelable" , self.tab1 , QtCore.QRect(258 ,  235 + 40 * 7, 97, 21) , font); 
        self.khaiValueBrowser = UI_Utility.Create_TextBrowser("khaiValueBrowser" , self.tab1 , QtCore.QRect(360, 190 + 40 * 8 , 211, 31));

        # 대기오염 상태 이미지
        self.Dustdisplay_img = UI_Utility.Create_Label("Dustdisplay_img" , self.tab1 , QtCore.QRect(20, 180, 221, 171) , font);

        # 코멘트
        self.Commentlabel = UI_Utility.Create_Label("Commentlabel" , self.tab1 , QtCore.QRect(120, 536, 101, 20) , font);
        self.CommentBrowser = UI_Utility.Create_TextBrowser("CommentBrowser" , self.tab1 ,QtCore.QRect(30, 410, 200, 121));
        
         #이메일 전송 버튼
        self.dustSendButton = UI_Utility.Create_PushButton("dustSendButton" , self.tab1 , QtCore.QRect(250, 550, 93, 28) , font);
        self.SendCheckBrowser = UI_Utility.Create_TextBrowser("SendCheckBrowser" , self.tab1 , QtCore.QRect(350, 550, 93, 28));

        #이미지
        self.pic1 = UI_Utility.Create_Label("pic1" , self.tab1 , QtCore.QRect(10, 30, 161, 141) , font);
        self.pic2 = UI_Utility.Create_Label("pic2" , self.tab1 , QtCore.QRect(480, 30, 161, 141) ,font);

        #메인 그림
        self.mainpic = UI_Utility.Create_Label("mainpic" , Dialog , QtCore.QRect(0, 0, 705, 150) , font);
        
       


        self.tabWidget.addTab(self.tab1, "대기오염")
        
        
#       이메일 선택
        self.tab_Email = UI_Utility.Create_Widget("tab_Email");    
        self.tabWidget.addTab(self.tab_Email , "EmailSetting");

        font = UI_Utility.Create_Font(setFamily = "휴먼매직체" , setPointSize = 15 );
        self.EmailMainlabel = UI_Utility.Create_Label( "EmailMainlabel" , self.tab_Email , QtCore.QRect(190, 40, 311, 41)  , font);
        
        self.IDEdit = UI_Utility.Create_TextEdit("IDEdit" ,  self.tab_Email , QtCore.QRect(240, 130, 201, 31));
        font = UI_Utility.Create_Font(setFamily = "휴먼매직체");
        self.IDlabel = UI_Utility.Create_Label( "IDlabel" , self.tab_Email , QtCore.QRect(150, 140, 71, 16)  , font);
        self.Passwordlable = UI_Utility.Create_Label( "IDlabel" , self.tab_Email , QtCore.QRect(150, 190, 71, 20)  , font);
        self.PasswordEdit = UI_Utility.Create_TextEdit("PasswordEdit" ,  self.tab_Email , QtCore.QRect(240, 190, 201, 31));

        self.SendTolabel = UI_Utility.Create_Label( "SendTolabel" , self.tab_Email , QtCore.QRect(150, 250, 64, 15)  , font);
        self.SendToEdit = UI_Utility.Create_TextEdit("SendToEdit" ,  self.tab_Email , QtCore.QRect(240, 250, 201, 31));

        self.MailTitlelable = UI_Utility.Create_Label( "MailTitlelable" , self.tab_Email , QtCore.QRect(150, 330, 64, 15)  , font);
        self.MailTitleEdit = UI_Utility.Create_TextEdit("MailTitleEdit" ,  self.tab_Email , QtCore.QRect(240, 320, 281, 71));
      
        self.SettingButton = UI_Utility.Create_PushButton("SettingButton" , self.tab_Email ,QtCore.QRect(240, 420, 93, 28) , font);
        self.SettingMsgBrowser =  UI_Utility.Create_TextBrowser("SettingMsgBrowser" , self.tab_Email , QtCore.QRect(180, 460, 211, 31));

        self.mailBox_Img = UI_Utility.Create_Label("mailBox" , self.tab_Email , QtCore.QRect(420, 420, 191, 151) , font);


        self.retranslateUI(Dialog);
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUI(self , Dialog) :
        self._translate = QtCore.QCoreApplication.translate;
        Dialog.setWindowTitle(self._translate("Dialog" , "기상청"));
        self.pushButton.setText(self._translate("Dialog" , "Search"))
        self.findustlabel.setText(self._translate("findustlabel" , "미세먼지 농도"));
        self.Ozonelabel.setText(self._translate("Ozonelabel" , "오존 농도"));
        self.nitrogendioxidelable.setText(self._translate("nitrogendioxidelable" , "이산화질소 농도"));
        self.coValuelable.setText(self._translate("coValuelable" , "일산화탄소 농도"))
        self.so2Gradelable.setText(self._translate("so2Gradelable" , "아황산가스 지수"));
        self.coGradelabel.setText(self._translate("coGradelabel" , "일산화탄소 지수"));
        self.o3Gradelabel.setText(self._translate("o3Gradelabel" , "오존 지수"));
        self.no2Gradelable.setText(self._translate("no2Gradelable" , "이산화질소 지수"));
        self.khaiValuelable.setText(self._translate("khaiValuelable" , "통합대기 수치"));
        self.Dustdisplay_img.setText(self._translate("Dustdisplay_img" , "이미지 출력"));
        self.Commentlabel.setText(self._translate(" self.Commentlabel" , "코멘트"));
        self.mainpic.setText(self._translate("mainpic" , "메인 이미지"));
        self.dustSendButton.setText(self._translate("dustSendButton" , "Send_Email"));
        #Email
        self.EmailMainlabel.setText(self._translate("EmailMainlabel"  , "E-Mail Account Setting"));
        self.IDlabel.setText(self._translate("IDlabel" , "ID(Gmail)"));
        self.Passwordlable.setText(self._translate("Passwordlable" , "Password"));
        self.SendTolabel.setText(self._translate("SendTolabel" , "SendTo"));
        self.MailTitlelable.setText(self._translate("MailTitlelable" , "Mail Title"));
        self.SettingButton.setText(self._translate("SettingButton" , "Setting"));