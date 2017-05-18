#-*- coding: utf-8 -*-

# �̸��� ���� �������� SMTP : 7��Ʈ �ƽ�Ű ���ڸ� ����
# MIME( Multipurpose Internet Mail Extensions) : ���� ���� ���ͳ� ǥ��
# ��� �ƴ� ���� ���̳ʸ� ����


import smtplib
from email.mime.text import MIMEText
smtpHost = "smtp.test.com" #smtp ���� �ּ�

text = "hello world";
msg = MIMEText(text); # �ؽ�Ʈ�� �⺻�� ������ �ϳ� �����մϴ�. text�� �ݵ��
                     # ASCII �ڵ忩�߸� �մϴ�. ���� unicode�� ��� �ִٸ� �޴� �ʿ��� ���ڰ� ����

senderAddr = "test@send.com" # ������ ��� email �ּ�
recipientAddr = "test@rec.com" # �޴� ��� email �ּ�


msg["Subject"] = "test email";
msg["From"] = senderAddr;
msg["To"] = recipientAddr;

#SMTP ������ �̿��� ���� �����ϴ�.
s = smtplib.SMTP(smtpHost);
s.connect();
s.sendmail(senderAddr , [recipientAddr] , msg.as_string());
s.close();
