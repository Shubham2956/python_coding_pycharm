class addition:
    def add(self,*args):
        total = 0
        for i in args:
            total = total+i
        print("total :",total)

obj = addition()
obj.add(20,44,343,223,2)




def m1():
    x = 0
    y = 1
    while True:
        yield x
        x,y = y,x+y
def show():
    for i in m1():
       if i <250:
            print(i)

m1()
show()

print("-------------------------------------fibonacci------------------------------------")


def gen ():
    x,y=0,1
    while True:
        yield x
        x,y=y,x+y
def show():
    for i in gen():
        if i <200:
            print(i)
print("fibo")
gen()
show()


print("--------------------------------------------fibo----------------------------------------")
