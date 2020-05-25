class Lib:
    def __init__(self):
        self.books=['apple','ball','cat']

    def disp(self):
        self.choice=int(input("1. Display 2. Borrow 3. Return 4. Exit"))

    def bor(self):
        self.bname= input("Type Book Name to borrow \n")
        if self.bname in self.books:
            print("Book Borrowed")
            self.books.remove(self.bname)
        else:
            print("Book unavailabe")
    
    def ret(self):
        self.bname= input("Type Book Name to return \n")
        self.books.append(self.bname)
        print("Book returned")

p1=Lib()

while True:
    p1.disp()

    if p1.choice == 1:
        print(p1.books)
    elif p1.choice == 2:
        p1.bor()
    elif p1.choice == 3:
        p1.ret()
    else:
        print("END")
        quit()


