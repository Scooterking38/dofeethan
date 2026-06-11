class animal:
    def __init__(self):
        self.x = 0
    def add(self,num):
        self.x += num
    def request(self):
        print(self.x)
    def mynuss(self,num):
        self.x -= num
ethan = animal()
elijah = animal()

ethan.add(1)
elijah.add(2)

ethan.add(3)
elijah.add(67)

ethan.request()
elijah.request()
ethan.mynuss(8)
elijah.mynuss(138)
ethan.request()
elijah.request()

#day2
class base:
    def request(self):
        print(self.x)
class animal(base):
    def __init__(self):
        self.x = 0
    def sub(self,num):
        self.x -= num
class inamil(base):
    def __init__(self):
        self.x = 0
    def add(self,num):
        self.x += num



        
ethan = animal()
elijah = inamil()

ethan.sub(6)
elijah.add(7)

ethan.request()
elijah.request()
