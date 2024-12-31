class arithmetic:
    def add(self,a,b):
        self.a = a
        self.b = b
        print(self.a+self.b)

    def substraction(self,a,b):
        self.a = a
        self.b = b
        print(self.a - self.b)

    def multiplication(self,a,b):
        self.a = a
        self.b = b
        print(self.a * self.b)

    def division(self,a,b):
        self.a = a
        self.b = b
        print(self.a / self.b)


obj = arithmetic()

obj.add(232,545)
obj.substraction(54545,43343)
obj.multiplication(4,5)
obj.division(100,10)



class operation:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)

    def substraction(self):
        print(self.a - self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

obj11 = operation(55,4)
obj11.add()
obj11.substraction()
obj11.multiplication()
obj11.division()



