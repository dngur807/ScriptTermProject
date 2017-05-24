#r=2
#
#circle_area = 3.14 *(r**2 )#**제곱
#x= 3
#y = 4
#triangle_area = x*y /2
#
#print(circle_area, triangle_area)

#print('이'+'제선')

#colors = ['red', 'green','golf']#리스트
#print(colors)
#
#colors += ['orange']
#print(colors)
#
#a = {1,2,3}
#b = {3,4,5}

#color = {"apple":"red","banana":"yellow"}
##print(color)
##print(color["apple"])
#
#for c in color.items():
#    print(c)
#print("---------------")
#for k ,v in color.items():
#    print(k,v)
#print("---------------")
#for v in color.values():
#    print(v)

#class CounterManager:
#    __insCount = 0
#    def __init__(self):
#        CounterManager.__insCount +=1
#    def staticPrintCount(self):#
#        print("Instance Count :  %d" %CounterManager.__insCount)
#    SPrintCount = staticmethod(staticPrintCount)
#
#
#print(CounterManager.__insCount)


#연산자 중복 정의 : - Sub
#class Gstring:
#  #  def __init__(self,init=None):
#        self.content = init
#    def __sub__(self,str):
#        for i in str:
#            self.content = self.content.replace(i,' ')
#    def Remove(self,str):
#        return self.__sub__(str)
#
#g= Gstring("ABCDEFGabcdefr")
#g  - "apple"
#g.Remove("A")
#
#print(g.content)

#class SuperClass: 	#부모 클래스
#    x = 10
#    def printX(self):
#        print(self.x)
#class SubClass(SuperClass): #자식 클래스
#    y = 20
#    def printX(self):   #메서드 오버라이딩
#        print("SubClass:", self.x)
#    def printY(self):
#        print(self.y)
#
#
#s = SubClass()
#s.a = 30#새 인스턴스 변수 추가
#s.x = 50
#print("{0},{1}".format(s.x,SubClass.x))
#print(s.__dict__) #


#다중 상속

#class Tiger:
#    def Jump(self):
#        print("호랑이처럼 멀리 점프하기")
#    def Cry(self):
#        print("호랑이 어흥")
#class Lion:
#    def Bite(self):
#        print("사자처럼 한입에 꿀꺽하기")
#    def Cry(self):
#        print("사자 으르렁")
#class Liger(Tiger, Lion):    #Tiger, Lion 순서대로
#    def Play(self):
#        print("라이거만의 사육사와 재미있게 놀기")
#
#
#l = Liger()
#l.Cry()#먼저 상속된것을 먼저 셀렉
#print(Liger.__mro__)

#class Animal:
#    def __init__(self):
#        print("Animal __init__(self)")
#class Tiger(Animal):
#    def __init__(self):
#        super().__init__()  # 부모 클래스 생성자 호출
#        print("Tiger __init__()")
#
#
#class Lion(Animal):
#    def __init__(self):
#        super().__init__()  # 부모 클래스 생성자 호출
#        print("Lion __init__()")
#
#
#class Liger(Tiger, Lion):
#    def __init__(self):#
#        super().__init__()  # 부모 클래스 생성자 호출
#        print("Liger __init__()")
#
#l = Liger()


class GString:
    def __init__(self,init = None):
        self.content = init
    def __sub__(self,str):
        for i in str:
            self.content = self.content.replace(i,' ')
        return GString(self.content)
    def __abs__(self):
        return GString(self.content.upper())
    def Print(self):
        print(self.content)

g = GString("aBcdef")

g -= "df"
g.Print()

g = abs(g)
g.Print()
































































