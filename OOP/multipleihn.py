class apple:
    kingdom="fruit"
    shape="oval"
class redapple():
    color="red"
    shape="circle"
class myapple(apple,redapple):
    flavor="sweet"
    def __init__(self):
        print("Kingdom= {} Color={} flavor= {} shape={} ".format(self.kingdom,self.color,self.flavor, self.shape))

m=myapple()
