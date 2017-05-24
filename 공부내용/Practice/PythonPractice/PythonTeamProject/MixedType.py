#-*- coding: utf-8 -*-

#테스트
import smtplib
import mimetypes
 
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


#global value
host = "smtp.gmail.com" 			#your smtp address
port    =   "587"
htmlFileName = "book.xml"
imageFileName = "빅뱅.gif"

senderAddr = "goflvhxj807@gmail.com"     		#������ ��� email �ּ�.
recipientAddr = "dngur807@naver.com"   		#�޴� ��� email �ּ�.

msg = MIMEBase("multipart" , "alternative");
msg["Subject"] = "Test email in Python 3.5";
msg["From"] = senderAddr;
msg["To"] = recipientAddr;



htmlFD = open(htmlFileName , 'rb');
HtmlPart = MIMEText(htmlFD.read() ,  _charset = "UTF-8");
htmlFD.close();


msg.attach(HtmlPart);

# ������ �߼��Ѵ�.
s = smtplib.SMTP(host,port);
s.ehlo();
s.starttls();
s.ehlo();
s.login(senderAddr , "akrmfls807");
s.sendmail(senderAddr , [recipientAddr] , msg.as_string());
s.close();
