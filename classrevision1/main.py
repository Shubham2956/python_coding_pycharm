class Product:
    def __init__(self):
        print("in to the init method")
    def show(self):
        print("in to the show method")


obj1 = Product()

obj1.show()



class New_Member:
    def __init__(self,name_of_member,age_of_member):
        self.name = name_of_member
        self.age = age_of_member
    def show(self):
        print(self.name)
        print(self.age)

ob = New_Member("shubham","22")
ob.show()

ob1 = New_Member("OMKAR","21")
ob1.show()


class employee():
    def __init__(self , e_id,e_name,e_address):
        self.id = e_id
        self.name = e_name
        self.address = e_address
    def details(self):
        print(self.id)
        print(self.name)
        print(self.address)

ob1_e = employee(101,"sagar","pune")
ob1_e.details()


class arithmetic():
    def __init__(self,a ,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mult(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)

objadd = arithmetic(10,40)
objadd.add()
objadd.sub()
objadd.mult()

objopr = arithmetic(50,90)
objopr.mult()


