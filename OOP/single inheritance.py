class fruit:
    
    living = "obvious"

    def yearr(self):
        self.year=1998
        print("Year =",self.year)

class apple(fruit):
    year=2020
    def ap(self):
        print("Living: {} \n Year: {}".format(self.living,self.year))

a=apple()
a.ap()
f=fruit()
f.yearr()
