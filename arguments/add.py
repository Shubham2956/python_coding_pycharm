pattern = int(input("enter the number for pattern:"))
def add():
    for i in range(pattern):
        for j in range(i+1):
            print("*",end = "")
        print(" ")

obj = add()

pat = int(input("enter the number :"))
def sub():
    for i in range(pat,0,-1):
        for j in range(0,i):

            print("*",end=" ")
        print(" ")

obj1  = sub()