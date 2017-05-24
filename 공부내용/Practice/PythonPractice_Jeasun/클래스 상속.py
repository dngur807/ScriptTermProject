class Person:   #부모 클래스
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber
    def PrintInfo(self):
        print("name : {0} , PhoneNumber : {1}".format(self.Name, self.PhoneNumber))

class Student(Person): #자식클래스 (Person에서 상속받음)
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self,name,phoneNumber)
        self.Subject = subject
        self.StudentID = studentID

    def PrintInfo(self):
        print("Name:{0}, Phone Number: {1}, subjet : {2}, id : {3}"
              .format(self.Name, self.PhoneNumber,self.Subject, self.StudentID))

student =Student("a","b","c","d")
person = Person("1","2")

#둘이 당연히 다른객체 니깐 다른 값이 나온다.
person.PrintInfo()
student.PrintInfo()

