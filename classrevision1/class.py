class add:
    def __init__(self):
        print("in init")


obj = add()

class newclass:
    def __init__(self):
        print("this is for __init__ purpose")

    def add(self, a, b,):
        print(a+b)



obj1 = newclass()
obj1.add(20,40)


