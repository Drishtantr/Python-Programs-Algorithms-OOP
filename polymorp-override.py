class Employee:
    def hrs(self):
        self.hr=80
        print("Employee time:",self.hr)

class Trainee(Employee):
    def hrs(self):
        self.hr=45
        print("Trainee time:",self.hr)

    def resett(self):
        super().hrs()

e=Employee()
e.hrs()
t=Trainee()
t.hrs()
t.resett()



