class add:
    a = 20
    b = 30
    def __init__(self,c,d):
        self.c = c
        self.d = d
    def show(self):
        print(self.c+self.d)


obj = add(20,40)
obj.show()
print(add.a)