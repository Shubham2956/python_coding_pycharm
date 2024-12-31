class newclass:
    def __init__(self,x,y,z):
        self.name = x
        self.mobile_no = y
        self.address = z
    def show(self):
        print(self.name)
        print(self.mobile_no)
        print(self.address)

obj1 = newclass("pratik","+91-6586584648","pune")
obj1.show()

obj2 = newclass("sangram","+91-5454342334","mumbai")
obj2.show()