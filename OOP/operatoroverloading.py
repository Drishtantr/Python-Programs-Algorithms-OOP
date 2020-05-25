class Square():
    def __init__(self,side):
        self.side=side

    def __add__(self,side):
        return(4*s1.side+4*s2.side)

s1=Square(5)
s2=Square(4)
print(s1+s2)        