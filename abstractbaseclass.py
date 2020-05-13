from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    line=4
    def area(self):
        print(self.line*self.line)

class Rec(Shape):
    linea=4
    lineb=5
    def area(self):
        print(self.linea*self.lineb)

s=Square()
r=Rec()
s.area()
r.area()
