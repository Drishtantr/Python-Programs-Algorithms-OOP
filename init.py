class Employee:
    def __init__(self,name,deg):
        self.name=name
        self.deg=deg

    def disp(self):
        print(self.name,self.deg)

e1=Employee("RAM","DEV")
e2=Employee("SAM","MAR")
e1.disp()
e2.disp()

