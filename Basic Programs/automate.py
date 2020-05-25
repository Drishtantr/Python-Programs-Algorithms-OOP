import random
class Guess:
    a=random.randint(0,10)
    def gue(self,b):
        if self.a is b:
            print("Wright")
        else:
            print("NOOO")

g=Guess()
b=input('Enter a no')
b=int(b)
g.gue(b)