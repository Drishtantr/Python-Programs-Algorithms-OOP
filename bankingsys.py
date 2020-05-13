import random

# print(random.randint(10000, 100000))

class Library:
    accounts=[]
    # for i in range(1,6):
    #     accounts.append(random.randint(10000, 100000))

    names=[]
    moneys=[]
    x=0

    
    def val(self,accno,name):
        if accno in self.accounts and name in self.names:
            print("Welcome\n")
            for accno in self.accounts:
                print("Acc no: ",accno)
                print("Name: ",name)
                print("Balance: ",self.moneys)
        else:
            print("User Not Found")


    def new(self,name,money):
        self.accounts.append(random.randint(10000, 100000))
        self.names.append(name)
        self.moneys.append(money)
        print("Your acc no is ",self.accounts[self.x])
        print("\nRegistered.Choose to login now \n")
        self.x=self.x+1



l=Library()

while True:
    ch=int(input("Welcome. Select:\n1. New User\n2. Login\n"))
    if ch is 1:
        name=input("Name: ")
        money=int(input("Money to Deposit: "))
        l.new(name,money)
    if ch is 2:
        name=input("Name: ")
        accno=int(input("Account no:  "))
        l.val(accno,name)
    if ch is 3:
        print(l.accounts)
        print(l.names)

