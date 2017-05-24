#-*- coding: utf-8 -*-

import PythonPractice16;



def ServerAccect() :
    import socket

    HOST = "0" # INADDR_IN # ȣ��Ʈ�� �������� ������ ������ ��� �������̽� �ǹ�
    PORT = 4000 #��Ʈ ����
    sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)# ���� ����
    sock.bind((HOST , PORT))
    sock.listen(1)

    conn, addr = sock.accept()

    print("Connected by" , addr)

    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close();


#ServerAccect();


#urllib url���� ��Ű�� , url �Ľ� , url �� �Ҵ�� ������ ������
from urllib.parse import urlparse

url = "http://search.naver.com/search.naver?where=nexearch&query=python&sm=top_hty&fbm=1"
parts = urlparse(url);
print(parts)

print(parts.path)

# 16�� ���� ���� ���α׷��� ���ͳ� ��� Ȯ��
# launcher.py( �޴� ����ϰ� ����� ��� �Է� �ޱ� )
# xmlbook.py ( xml ���� ��� ���� )
# internetbook.py ( ���ͳ� ���� ��� ����)
 

# OpenAPI �̿��Ͽ� å ���� ���� ����

# https://apis.daum.net/search/book?apikey=<���Ű>&q=love&output=xml
# �� �������� ���� OpenAPI ��� ����� XML ������ �ƴ϶� HTML �������� ���
# �� URL�� ���̽㿡�� �����ϸ� �������� XML ������ ��µ�
# ���̽㿡�� OpenAPI �̿��� (http.client , http.server2�� ��� �ʿ�)


# HTTPConnection.request(<method> , <url> [ , <body>[, [headers>]]);

from http.client import HTTPConnection
import http.client
conn = http.client.HTTPConnection("apis.daum.net");
conn.request("GET" , "/search/book?apikey=c65f7d130ef99a3dd1826fde11f9b0b3&q=love&output=xml");

#������ GET ��û
req = conn.getresponse() # openAPI �������� ������ ��û�� �޾ƿ�
print(req.status , req.reason );

cLen = req.getheader("Content-Length"); # ������ ������ ����
#print(req.read(cLen));# ������ �ϱ�


# ��� �߰� : ����ڰ� ISBN�� �Է��ϸ� �ش� å ������ OpenAPI �˻�����
# ������ å ������ XML�� �����ϴ� ���
# ���� OpenAPI ��� ��� XML ���� : ��°�� �ʵ� (response filed)



# getBookDataFromISBN(isbn) �Լ� : ������ �ʿ��� ������ URL�� ��û�ϰ�
# XML ������ ����޴� ����

regKey = 'c65f7d130ef99a3dd1826fde11f9b0b3' #���� OpenAPI Ű
server = "apis.daum.net"      		  #���� OpenAPI ����
conn = None;


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getBookDataFromISBN(isbn) :
    global server , regKey , conn;
    if conn == None:
        connectOpenAPIServer() # OpenAPI ����
    # uri = userURIBuilder(Server , key = regKey , query = "%20" , display = "1"
    #    , start = "1" , target = "book_adv" , d_isbn = isbn); #���̹� ISBN���� ������ URL ����


    uri = userURIBuilder(server , apikey = regKey , q = isbn , output = "xml") # ���� �˻� URL
    conn.request("GET" , uri);

    req = conn.getresponse();
    print(req.status);
    if int(req.status) == 200:
        print("Book data downloading compleate! ");
        return extractBookData(req.read()) # ��û�� �����̸� book���� ����
    else :
        print("OpenAPI request has been failed! please retry");
        return None;

# OpenAPI �� ���� ������ XML �������� isbn�� title�� ����
def extractBookData(strXML) : 
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXML);
    print(strXML);
    # Book������Ʈ�� �����ɴϴ�.
    itemElements = tree.getiterator("item");        #itme ������Ʈ ����Ʈ ����
   # print(itemElements);

    for item in itemElements:
        isbn = item.find("isbn");
        strTitle = item.find("title");

        print(strTitle);
        if len(strTitle.text) > 0:
            return {"ISBN" : isbn.text , "title" : strTitle.text} # ���� ���� ��ȯ


def userURIBuilder(server , **user):

#"/search/book?apikey=c65f7d130ef99a3dd1826fde11f9b0b3&q=love&output=xml"

    #URL �ּ�
    str = "https://" + server + "/search/book" + "?" + "apikey=" + user.get("apikey") + "&q=" +user.get("q") + "&output=" + user.get("output"); #���� �˻� URL
    return str;


# Naver Open API�� �̿��Ͽ� å ���� ��������
# ����� ���Ե� å �˻�
import os
import sys
import urllib.request




#"https://openapi.naver.com/v1/search/book_adv.xml?d_isbn=" + isbn # xml




# getBookDataFromISBN : ������ �ʿ��� ������ URL�� ��û�ϰ� XML ������ ����޴� ����

#def getBookDataFromISBN2(isbn) : 
#    client_id = "NrkKI0dzkjbVyJJaGGg1"
#    client_secret = "bxP7XUH_Sh"
#    #isbn        =   "0596513984"
#   # encText = urllib.parse.quote("���");
#    url = "https://openapi.naver.com/v1/search/book_adv.xml?d_isbn="+isbn;
    
    

#    import urllib.request    
#    request = urllib.request.Request(url);   
#    request.add_header("X-Naver-Client-Id", client_id);
#    request.add_header("X-Naver-Client-Secret", client_secret); 
#    response = urllib.request.urlopen(request);

  




def main():
    flag = 1;
   
   # PythonPractice16.BooksDoc = PythonPractice16.LoadXMLFromFile()


    while flag :
        print("----------------------------------------");
        print("print Book list: b")
        print("Get book data from isbn : g");
        print("send maIl : i");
        print("sTart Web Service: t");
        print("----------------------------------------");
        select =input("select menu :");
        
        if select == "q" :
            flag = 0;
        elif select == "g":
            isbn = input("input isbn to get :");
            getBookDataFromISBN(isbn);
        elif select == "b":
            PythonPractice16.PrintBookList(["title" ,]);

#main();