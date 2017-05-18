#-*- coding: utf-8 -*-

import xml.parsers.expat
from xml.dom.minidom import*


def start_element(name , attrs):
    print("Start Element : " , name , attrs);

def char_data(data):
    print("Character data" , repr(data));

pa = xml.parsers.expat.ParserCreate(); 
pa.StartElementHandler = start_element;

pa.CharacterDataHandler = char_data;



pa.Parse("""<?xml version="1.0"?><book ISBN = "1111">
.. <title>Loving Python</title></book>""");



#메소드 이름 xml.dom.minidom.parse(file , parser)
# file로 부터 XML문서를 읽어서 Document 객체를 반환합니다.
# Parser 인수가 주어지면 minidom의 기본 파서가 아닌 사용자가 원하는 파서를 사용할
# 수 있습니다. (파서는 SAX2 parser객체만 사용 가능합니다.)

# xml.dom.minidom.parseString(data, parser); 
#parser()와 비슷하지만 입력으로 파일 대신 문자열을 받습니다.



xmlsrc = """ <item>
...<name>test</name>
...</item>
"""

doc = parseString(xmlsrc);  #문자열 입력 파싱 함수 , DOC 객체 반환
#print(doc);
#print(doc.toxml());
#print("\n\n");

names = doc.getElementsByTagName("name");#name 인 엘리먼트 가져옴
#print(names);
#print(names.length);



# -*- coding: cp949 -*-
from xml.dom.minidom import parse , parseString # minidom 파싱함수 임포트
from xml.etree import ElementTree

#### global
loopFlag = 1            # 무한 루프 제어변수
xmlFD = -1              # XML 문서 파일 디스크립터
BooksDoc = None         # XML 문서 파싱한 후 반환된 DOC 객체 변수



# LoadXMLFromFile() : minidom 메서드 XML 문서 파싱하고 전역변수 BooksDoc에 저장
# BooksFree() : 사용후에는 unlink() 메서드 호출해 DOM 객체 내부의 참조를 제거

def LoadXMLFromFile():
   # fileName = input("please input file name to load : ");
    fileName = "book.xml";
    global xmlFD;

    try:
        xmlFD = open(fileName); # XML 문서 open
    except IOError :
        print("invalid file name or path");
        return None;
    else :
        try:
            dom = parse(xmlFD);
        except Exception :
            print("loading fail!!");
        else :
            print("XML Document loading complete");
            return dom;
    return None;



def BooksFree() :
    if checkDocument():
        BookDoc.unlink();   # minidom 객체 해제

# toxml() 메서드를 이용해서 DOM 객체를 XML 문서로 변환
def PrintDOMtoXML():
 
    if checkDocument():
        print(BooksDoc.toxml());
        

from xml.dom.minidom import parse, parseString
books = parse("book.xml");      # DOC 객체
booklist = books.childNodes  # books의 자식노드 = 루트 엘리먼트

print(type(booklist) ) ;

print( len(booklist) ) ;


print(booklist[0]); # NodeList이므로 배열을 사용해 각 노드에 접근

print(booklist[0].nodeType) #nodeType == 1 (ELEMENT_NODE)

book = booklist[0].childNodes; # booklist의 자식노드



# PrintBookList(tags) : 책 목록 출력 (tags 리스트를 인자로 받아 매칭)
def launcherFunction(menu) : 
    if menu == "I" :
        BooksDoc = LoadXMLFromFile();
    elif menu == "b":
        PrintBookList(["title" ,]);

def checkDocument():
    return BooksDoc;

# 책 목록 출력
def PrintBookList(tags) :
    global      BooksDoc;
    if not checkDocument():
        return None;


    booklist = BooksDoc.childNodes;
    book     = booklist[0].childNodes;

    for item in book :
        if item.nodeName == "book":     # 엘리먼트를 중 book 인 것을 추출
            subitems = item.childNodes; # book에 들어 있는 노드들을 가져옴
            for atom in subitems :
              if atom.nodeName in tags:
                print("title ==" , atom.firstChild.nodeValue);


# 엘리먼트 : XML 문서는 엘리먼트로 이루어져 있음


# AddBook(bookdata) : 인자로 사전 { "ISBN ": ISBN , "title" : title }을 입력받음
    # 새로운 도서 등록 : 하나의 도서 데이터는 book 엘리먼트와 하위 엘리먼트로 구성됨

def AddBook(bookdata):
    global BooksDoc;
    if not checkDocument () :
        return None;

    newBook = BooksDoc.createElement("book");
    newBook.setAttribute("ISBN" , bookdata["ISBN"]); # ISBN 속성 설정
    titleEle = BooksDoc.createElement("title"); # Title 엘리먼트 생성

    titleNode = BooksDoc.createTextNode(bookdata["title"]) # TextNode 생성

    try :
        titleEle.appendChild(titleNode); #텍스트 노드와 Title 엘리먼트를 연결
    except Exception:
        print("append Child fail - please check the parent element & node!!");
        return None;
    #else :
    #    titleEle.appendChild(titleNode);

    try :
        newBook.appendChild(titleEle); # titleNode를 book 엘리먼트와 연결
        booklist = BooksDoc.firstChild;
    except Exception:
        print ("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if booklist != None:
            booklist.appendChild(newBook) # newBook을 booklist 엘리먼트와 연결


# 검색 인자로 입력받은 keyword로 title 검색한 후 (ISBN , Title) 리스트 출력

def SearchBookTitle(keyword):
    global BooksDoc;
    retlist = [];
    if not checkDocument():
        return None;

    try : 
        # fromstring 문자열 text를 파싱 ElemntTree 객체 반환
        tree = ElementTree.fromstring(str(BooksDoc.toxml())); #ElementTree 모듈 함수
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None;

    # Book 엘리먼트 리스트를 가져 옵니다.
    # getiterator   - 현재 엘리먼트의 하위 엘리먼트를 모두 가져옴 tag 가 
    # 지정되어 있으면 tag에 해당하는 엘리먼트만 반환

    bookElements = tree.getiterator("book") #ElementTree 객체 메서드
    for item in bookElements :
        strTitle = item.find("title");      # title 엘리먼트 추출
        if (strTitle.text.find(keyword) >= 0) : # keyword 검색 해당 키 있는거 모두 추가
            retlist.append((item.attrib["ISBN"] , strTitle.text)); # 리스트에 (ISBN , title) 추가ㅣ

    print(retlist);
    return retlist;

        

# XML 문서를 HTML 로 변환하기
# MakeHtmlDoc(BookList) 함수 : DOM 객체를 생성하고 
# 부모 엘리먼트와 자식 엘리먼트를 생성해
# DOM객체에 추가


def MakeHtmlDoc(BookList) :
    from xml.dom.minidom import getDOMImplementation

    BookList = SearchBookTitle(BookList);
    # DOM 개체를 생성
    impl = getDOMImplementation()
    
    newdoc = impl.createDocument(None, "html", None)#HTML 최상위 엘리먼트 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성
    body = newdoc.createElement('body')


    for bookitem in BookList:
        b = newdoc.createElement('b'); # Bold 엘리먼트 생성
        ibsnText = newdoc.createTextNode("ISBN:" + bookitem[0])
        b.appendChild(ibsnText);
        body.appendChild(b);
        br = newdoc.createElement('br') 		     # <br> 부분을 생성
        body.appendChild(br)

        p = newdoc.createElement('p')                                  # title 부분을 생성
        titleText= newdoc.createTextNode("Title:" + bookitem[1]) # 텍스트 노드 생성
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  # <br> 부분을 부모 엘리먼트에 추가
        
  
    top_element.appendChild(body) # Body 엘리먼트를 최상위 엘리먼트에 추가
    print(newdoc.toxml());
    return newdoc.toxml()



def main() :
    print("Welcome! Book Manager Program (xml version)")

    global loopFlag # 꼭 선언하자'
    global BooksDoc
    BooksDoc = LoadXMLFromFile()

    while (loopFlag):
        print("========Menu==========")
        print("Load xml:  l")
        print("Print dom to xml: p")
        print("Quit program:   q")
        print("print Book list: b")
        print("Add new book: a")
        print("sEarch Book Title: e")
        print("Make html : m")
        print("==================")
        inp = str(input("select menu : "))
        
        if inp == "q" :
            loopFlag = 0#종료
        elif inp == "p" :
            PrintDOMtoXML()   
        elif inp == "b" :
            PrintBookList(["title" ,])   

        elif inp == 'a':
            ISBN = input("insert ISBN : ")
            title = input("insert Title : ")
            AddBook({"ISBN" : ISBN , "title" : title})
        elif inp == "e":
            key = input("input keyword to search :")
            SearchBookTitle(key)
        elif inp == "m":
            key = input("input keyword to html :")
            MakeHtmlDoc(key);

#main();

