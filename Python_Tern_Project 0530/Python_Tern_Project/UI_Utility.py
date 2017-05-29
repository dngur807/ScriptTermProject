

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore , QtGui , QtWidgets

#def Create_Font(family , weight):
#    font = QtGui.QFont(family);
#    font.setWeight(weight);
#    return font;

def Create_Font(**argv):
    if argv.get("setFamily") == None :
        return None;
    font = QtGui.QFont(argv.get("setFamily"));
    if argv.get("setPointSize") != None :
        font.setPointSize(argv.get("setPointSize"));
    if argv.get("setBold") != None :
        font.setBold(argv.get("setBold"));
    if argv.get("setWeight" ) != None:
        font.setWeight(argv.get("setWeight" ));

    if argv.get("setItalic" ) != None:
        font.setItalic(argv.get("setItalic" ));
    if argv.get("setUnderline" ) != None:
       font.setItalic(argv.get("setUnderline" )); 
    return font;


def Create_TabWidget(Dialog , objName , rcRect , font):
    TabWidget = QtWidgets.QTabWidget(Dialog);
    TabWidget.setGeometry(rcRect);
    TabWidget.setFont(font);
    TabWidget.setObjectName(objName);
    return TabWidget;

def Create_Widget(objname):
    tab = QtWidgets.QWidget();
    tab.setObjectName(objname);
    return tab;

def Create_PushButton(objname , tab , rcRect , font) :
    Button = QtWidgets.QPushButton(tab);
    Button.setGeometry(rcRect);
    Button.setFont(font);
    Button.setObjectName(objname);
    return Button;

def Create_TextEdit(objname , tab , rcRect) :
    textEdit = QtWidgets.QTextEdit(tab);
    textEdit.setGeometry(rcRect);
    textEdit.setObjectName(objname);
    return textEdit;

def Create_TextBrowser(objname , tab , rcRect):
    textBrowser = QtWidgets.QTextBrowser(tab);
    textBrowser.setGeometry(rcRect);
    textBrowser.setObjectName(objname);
    return textBrowser;

def Create_Label(objname , tab , rcRect , font):
    label = QtWidgets.QLabel(tab);
    label.setGeometry(rcRect);
    label.setFont(font);
    label.setObjectName(objname);
    return label;

def Create_ComboBox(objname , tab , rcRect):
    combo = QtWidgets.QComboBox(tab);
    combo.setGeometry(rcRect);
    combo.setObjectName(objname);
    return combo;

    