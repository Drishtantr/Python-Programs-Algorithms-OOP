class apple:
    kingdom="fruit"
class redapple(apple):
    color="red"
class myapple(redapple):
    flavor="sweet"
    def __init__(self):
        print("Kingdom= {} Color={} flavor= {} ".format(self.kingdom,self.color,self.flavor))

m=myapple()
