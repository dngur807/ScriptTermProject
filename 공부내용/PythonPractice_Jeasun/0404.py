str = "Not Calss Member"
class GString:
    str =""
    def Set(self,msg ):
            self.str = msg
    def Print(self):
            print(self.str)




g = GString()
g.Set("First Message")
g.Print()

g.str

GString.str

class MyClass:
    def __init__(self,value):
            self.Value = value
            print("Class is created Value = ",value)
    def __del__(self):
            print("Class is deleted")

def foo():
    d = MyClass(10)

foo()







