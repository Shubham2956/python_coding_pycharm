from abc import *
class a1(ABC):
    @abstractmethod
    def add(self):
        pass
    def mult(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class a2(a1):
    def add(self,a,b):
        self.a = a
        self.b = b
        print(f"addition of {a} and {b} is :",a+b)

    def mult(self,s,t):
        self.s = s
        self.t = t
        print(f"multiplicatio of {s} and {t} is :",s*t)


    def sub(self, m, n):
        self.m = m
        self.n = n
        print(f"substraction of {m} and {n} is :", m - n)





obj = a2()
obj.add(20,40)

obj.sub(30,20)

