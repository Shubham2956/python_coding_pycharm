# types of variables
# 1. instance variables ---it is also called as "OBJECT LEVEL VARIABLE" it changes object to object.
# 2. static variables ----it is also called as "CLASS LEVEL VARIABLE"
# 3. local variables ----it is also called as "METHOD LEVEL VARIABLE"


#instance variable

class emp:
    def __init__(self,emp_name,age):
        self.emp_name = emp_name
        self.age = age
    def show(self):
        print(self.emp_name)
        print(self.age)

obj = emp("mayur",101)   #value changes object to object
obj.show()

e1 = emp("prasad",102)      #other object
e1.show()
print("______________________________________________________________________________________________")


class play:
    def __init__(self):
        self.football = 500
        self.batball = 700
    def show(self):
        self.basketball  = 300
        print(self.football)
        print(self.batball)
        print(self.basketball)
o=play()

o.name = "arun"
o.show()
print("______________________________________________________________________________________________")


class emp:
    def __init__(self):
        self.x = 100    # inside constructor
        self.y = 200    #inside constructor
    def show(self):
        self.c = 600    # inside instance method
        print(self.x)
        print(self.y)
        print(self.c)
obj = emp()
obj.name = "arun"     # outside the class with the help of object reference
print(obj.name)
obj.show()
print(obj.__dict__)
print("______________________________________________________________________________________________")
 



class emp1:
    def __init__(self,name,id):
        self.name = name  # inside constructor
        self.id = id   #inside constructor
    def show(self, age):
        self.age = age   # inside instance method
        print(self.name)
        print(self.id)
        print(self.age)

obje = emp1("shubham",11022)
obje.addr = "pune"   # outside the class
print(obje.addr)
obje.show(21)
print("______________________________________________________________________________________________")


class material:
    def __init__(self):
        self.blackboard = 1400
        self.pen = 500
    def show(self):
        print(self.blackboard)
        print(self.pen)
        self.chair = 455
        print(self.chair)

obj = material()
obj.laptop =14000
print(obj.laptop )
obj.show()
print(obj.__dict__)
print("______________________________________________________________________________________________")


class company:
    def __init__(self,name,address,contact_no):
        self.name = name
        self.address = address
        self.contact_no = contact_no
    def show(self,ratings):
        self.ratings = ratings
        print(self.name)
        print(self.address)
        print(self.contact_no)
        print(self.ratings)

obj = company("rieter","pune",98667565)
obj.product = "sewing machine "
obj.show(9)
print(obj.product)
print("______________________________________________________________________________________________")


class employee:
    def __init__(self):
        self.id = 101
        self.name = "arun"
    def show(self):
        self.address = "pune"
        print(self.name)
        print(self.id)
        print(self.address)


obj = employee()
obj.join = 2022
obj.show()
print(obj.join)
print("______________________________________________________________________________________________")


class emp1:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def show(self,join):
        self.join = join
        print(self.id)
        print(self.name)
        print(self.join)

obj = emp1(101,"akash")
obj.address = "pune"
obj.show(2023)
print(obj.address)
print("______________________________________________________________________________________________")


class newinsvariable:
    def __init__(self):
        self.tenisball = 70
        self.basketball = 500
        self.volleyball = 350
        self.spungeball = 50
    def showobj(self):
        self.football = 700
        print(self.tenisball)
        print(self.basketball)
        print(self.volleyball)
        print(self.spungeball)
        print(self.football)

obj1 = newinsvariable()
obj.handball = 450
print(obj.handball)
obj1.showobj()
print("______________________________________________________________________________________________")


class newinsvariobj:
    def __init__(self,name,employee_id,address):
        self.name = name
        self.emp_id = employee_id
        self.address = address
    def showobj(self,blood_grp):
        self.blood_grp = blood_grp
        print(self.name)
        print(self.emp_id)
        print(self.address)
        print(self.blood_grp)

objshow = newinsvariobj("ankit","10222EERE","PUNE")
objshow.adharcard_no = "1232324543545"
objshow.showobj("A+")
print(objshow.adharcard_no)

print("______________________________________________________________________________________________")



class login:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print("login successfully")
    def show(self):
        print(f"login by {self.username}")
        print(f"password is {self.password}")

obj = login("admin-shubham","1234343")
obj.show()

