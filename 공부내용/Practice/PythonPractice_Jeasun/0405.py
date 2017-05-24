#-----------정보은닉-----------
#class CounterManager:
#    __insCount = 0
#    def __init__(self):
#        CounterManager.__insCount+=1
#    def staticPrintCount(self):
#        print("Instance Count : %d % CounterManager.__insCount")
#    SPrintCount = staticmethod(staticPrintCount)
#
#
#print(CounterManager.__insCount)

#-----------연산자 중복-----------

#class GString:
#	def __i#nit__(self, init=None):
#		self.content = init 	#인스턴스 변수 추가
#	def __sub__(self, str):	#'-' 연산자 중복 정의
#		for i in str:
#			self.content = self.content.replace(i,'')
#		return GString(self.content)
#	def Remove(self, str):
#		return self.__sub__(str)
#
##인스턴스 생성
#g = GString("ABCDEFGabcdefg")
##제작 함수1
#g - "Adg"
##제작 함수2
#g.Remove("Adg")


#class GString:
#    def __init__(self, init=None):
#        self.content = init         	#인스턴스 멤버변수 추가
#    def __sub__(self, str):         	#'-'연산자 중복
#  #      for i in str:
#            self.content = self.content.replace(i,'')
#        return GString(self.content)
#    def __abs__(self):              	#abs() 내장 함수 중복
#        return GString(self.content.upper())
#    def Print(self):
#        print(self.content)
#
#g = GString("aBcdef")
#g -= "df"       	#'-'연산자 중복된 경우 '-='도 지원
#g.Print()       	#출력결과: aBce
#g = abs(g)
#g.Print()       	#출력결과: ABCE


#class Sequencer:
#    def __init__(self,maxValue):
#        self.maxValue = maxValue
#    def __len__(self):
#        return self.maxValue
#    def __getitem__(self, index):
#        if(0<index<=self.maxValue):
#            return index*10
#        else:
#            raise IndexError("Index out of range")
#    def __contains__(self,item):
#        return (0<item<=self.maxValue)
#
#s = Sequencer(5)
#print(s[1])
#print(s[3])
#
#
#for i in range(1,5):
#    print(i);

#-----------상속-----------
class Person:   #부모 클래스
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber

    def PrintInfo(self):  # 메서드 오버라이딩 Person의 PrintInfo()재정의
        print("PersonInfo(Subject:{0}, Student ID:{1})".format(self.Subject, self.StudentID))

    def PrintPersonData(self):
        print("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))



class Student(Person): #자식클래스 (Person에서 상속받음)
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self,name,phoneNumber) #부모 클래스 생성자 호출
					#self명시 언바운드 메서드
        self.Subject = subject
        self.StudentID = studentID

    def PrintInfo(self):  # 메서드 오버라이딩 Person의 PrintInfo()재정의
        Person.PrintInfo(self)  # Person의 PrintInfo 언바운드 호출
        print("StudentInfo(Name:{0}, Phone Number:{1})".format(self.Name, self.PhoneNumber))
        print("StudentInfo(Subject:{0}, Student ID:{1})".format(self.Subject, self.StudentID))
    def PrintStudentData(self): #새로운 메서드 추가
        print("Student(Subject: {0}, Student ID: {1})".format(self.Subject,self.StudentID))


s = Student("Derick", "010-123-4567", "Computer", "990999")
#s.PrintPersonData()
#s.PrintStudentData()
s.PrintInfo()