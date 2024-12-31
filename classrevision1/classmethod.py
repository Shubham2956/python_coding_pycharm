class emp:
    company_name = "IBM"
    company_reg_no = 43234341
    company_tel_no = "+914443333"
    company_address = "pune"

    @classmethod
    def show(cls):
        print(cls.company_name)
        print(cls.company_reg_no)
        print(cls.company_tel_no)
        print(cls.company_address)

emp.show()
print("_____________________________________________________________________________________________________________")


class clasmethod:
    comp_name = "XYZ"
    comp_reg_no = "MHGGHKR443433423"
    comp_address = "pune"

    def noraml(self):
        clasmethod.comp_work = "technical"
        clasmethod.comp_phone_no = "+91-65633423"
        print(clasmethod.comp_work)
        print(clasmethod.comp_phone_no)

    @classmethod
    def staticshow(cls):
        print(cls.comp_name)
        print(cls.comp_reg_no)
        print(cls.comp_address)


clasmethod.staticshow()
obj = clasmethod()
obj.noraml()

print("_____________________________________________________________________________________________________________")

class newmethod:
    comp_name = "inxys"
    def __init__(self):
        self.id = "101"
        self.addr = "pune"

    def show(self):
        print(self.id,self.addr)

    @classmethod
    def newshow(cls):
        print(cls.comp_name)

obj = newmethod()
obj.show()
obj.newshow()

print("_____________________________________________________________________________________________________________")


class newobj:
    name = "omkar"
    father = "rajesh"
    suname = "kshirsagar"
    home = "shirwal"

    @classmethod
    def show(cls):
        print(cls.name,cls.father,cls.suname,cls.home)

newobj.show()