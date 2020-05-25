class Car:
    name="Public"
    _name="Protected"
    __name="Private"

class BMW(Car):
    def __init__(self):
        print(self.name)
        print(self._name)
        # print(self._Car__name)

c=Car()
print(c.name)
print(c._name)
print(c._Car__name)

d=BMW()
