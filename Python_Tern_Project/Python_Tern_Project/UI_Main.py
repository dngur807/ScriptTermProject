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
        
        font = UI_Utility.Create_Font(setFamily = "휴먼매직체" , setWeight = 75  , setBold = True , setPointSize = 18 , setItalic = False , setUnderline = False);
        self.CurTimeLabel = UI_Utility.Create_Label("CurTimeLabel" , self.tab1 ,  QtCore.QRect(230 , 130, 550 , 20) , font);



        #self.textEdit_4 = UI_Utility.Create_TextEdit("textEdit_4" ,  self.tab1 , QtCore.QRect(180, 30, 291, 31));# 찾기 검색 하는 곳

        #self.textBrowser_2 = UI_Utility.Create_TextBrowser("textBrowser_2" , self.tab1 , QtCore.QRect(310, 120, 151, 31));

        self.textBrowser_4 = UI_Utility.Create_TextBrowser("textBrowser_4" , self.tab1 , QtCore.QRect(360, 190, 211, 31));
        self.textBrowser_5 = UI_Utility.Create_TextBrowser("textBrowser_5" , self.tab1 , QtCore.QRect(360, 230, 211, 31));
        self.textBrowser_6 = UI_Utility.Create_TextBrowser("textBrowser_6" , self.tab1 , QtCore.QRect(360, 270, 211, 31));
        self.textBrowser_7 = UI_Utility.Create_TextBrowser("textBrowser_7" , self.tab1 , QtCore.QRect(360, 310, 211, 31)); 
        self.textBrowser_8 = UI_Utility.Create_TextBrowser("textBrowser_8" , self.tab1 , QtCore.QRect(360, 350, 211, 31)); 

        
        
        self.label_6 = UI_Utility.Create_Label("label_6" , self.tab1 , QtCore.QRect(280, 195, 71, 21) , font);
        
        
        font = UI_Utility.Create_Font(setFamily = "휴먼매직체" , setWeight = 75  , setBold = True , setPointSize = 11);
        self.label_7 = UI_Utility.Create_Label("label_7" , self.tab1 , QtCore.QRect(50, 410, 211, 1211) , font);



        self.textBrowser_9 = UI_Utility.Create_TextBrowser("textBrowser_9" , self.tab1 , QtCore.QRect(50, 410, 211, 121));
        self.textBrowser_10 = UI_Utility.Create_TextBrowser("textBrowser_10" , self.tab1 , QtCore.QRect(360, 470, 211, 31));
        self.textBrowser_11 = UI_Utility.Create_TextBrowser("textBrowser_11" , self.tab1 , QtCore.QRect(360, 430, 211, 31));
        self.textBrowser_12 = UI_Utility.Create_TextBrowser("textBrowser_12" , self.tab1 , QtCore.QRect(360, 510, 211, 31));
        self.textBrowser_13 = UI_Utility.Create_TextBrowser("textBrowser_13" , self.tab1 , QtCore.QRect(360, 390, 211, 31)); 

        font = UI_Utility.Create_Font(setFamily = "휴먼매직체" , setWeight = 75  , setBold = True , setPointSize = 11); 
        self.label_8 = UI_Utility.Create_Label("label_8", self.tab1 , QtCore.QRect(120, 365, 101, 21) , font);       
        self.label_9 = UI_Utility.Create_Label("label_9", self.tab1 , QtCore.QRect(120, 536, 101, 20) , font);
        self.label_10 = UI_Utility.Create_Label("label_10", self.tab1 , QtCore.QRect(280, 235, 64, 20) , font);
        self.label_11 = UI_Utility.Create_Label("label_11", self.tab1 , QtCore.QRect(280, 315, 64, 20) , font);
        self.label_12 = UI_Utility.Create_Label("label_12", self.tab1 , QtCore.QRect(280, 274, 64, 21) , font);
        self.label_13 = UI_Utility.Create_Label("label_13", self.tab1 , QtCore.QRect(280, 400, 64, 15) , font);
        self.label_14 = UI_Utility.Create_Label("label_14" , self.tab1 , QtCore.QRect(280, 475, 64, 20) ,font);
        self.label_15 = UI_Utility.Create_Label("label_15" , self.tab1 , QtCore.QRect(280, 435, 64, 20) ,font);
        self.label_16 = UI_Utility.Create_Label("label_16" , self.tab1 , QtCore.QRect(280, 355, 71, 21) ,font);
        self.label_17 = UI_Utility.Create_Label("label_17" , self.tab1 , QtCore.QRect(280, 516, 81, 20) ,font);



        self.pushButton_5 = UI_Utility.Create_PushButton("pushButton_5" , self.tab1 , QtCore.QRect(250, 550, 93, 28) , font);
        self.textBrowser_15 = UI_Utility.Create_TextBrowser("textBrowser_15" , self.tab1 , QtCore.QRect(350, 550, 191, 31));

        self.display_img = UI_Utility.Create_Label("display_img" , self.tab1 , QtCore.QRect(50, 180, 221, 171) , font);


        
        self.pic1 = UI_Utility.Create_Label("pic1" , self.tab1 , QtCore.QRect(10, 30, 161, 141) , font);
        self.pic2 = UI_Utility.Create_Label("pic2" , self.tab1 , QtCore.QRect(480, 30, 161, 141) ,font);

        
        self.tabWidget.addTab(self.tab1, "대기오염")

        self.tab_4 = UI_Utility.Create_Widget("tab_4");
        self.textEdit_7 = UI_Utility.Create_TextEdit("textEdit_7" , self.tab_4 , QtCore.QRect(190, 50, 291, 31)  );

        font = UI_Utility.Create_Font(setFamily = "휴먼매직체" , setWeight = 75  , setBold = True ); 
        self.pushButton_4 = UI_Utility.Create_PushButton("pushButton_4" , self.tab_4 , QtCore.QRect(290, 100, 93, 28) , font);

        self.textBrowser = UI_Utility.Create_TextBrowser("textBrowser" , self.tab_4 , QtCore.QRect(40, 140, 591, 371));
        self.ingrePic2 = UI_Utility.Create_Label("ingrePic2" , self.tab_4 , QtCore.QRect(490, 20, 161, 101) , font);

        self.pushButton_6 = UI_Utility.Create_PushButton("pushButton_6" , self.tab_4 , QtCore.QRect(210, 540, 93, 28) , font);

        self.textBrowser_16 = UI_Utility.Create_TextBrowser("textBrowser_16", self.tab_4 , QtCore.QRect(310, 540, 191, 31) );
        self.tabWidget.addTab(self.tab_4 , "");###############

       # self.tab_2 = UI_Utility.Create_Widget("tab_2");


     

        self.retranslateUI(Dialog);
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUI(self , Dialog) :
        self._translate = QtCore.QCoreApplication.translate;
        Dialog.setWindowTitle(self._translate("Dialog" , "기상청"));
        self.pushButton.setText(self._translate("Dialog" , "Search"))
    



