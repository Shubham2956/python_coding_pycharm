# static variables --- static variables also called as class variables





class emp:
    comp_name = "ISRO"
    comp_Reg_No = "01230323"
    def __init__(self, name,age):
        self.name = name
        self.age = age
        emp.addr = "LOCATION - MUMBAI"
    def show(self):
        print("name :", self.name)
        print("age", self.age)
        print("Company name :", emp.comp_name)
        print("company reg no :" , emp.comp_Reg_No)
        print("company address:", emp.addr)


obj1 = emp("shuham",21)
obj1.show()
print(obj1.__dict__)
print("______________________________________________________________________________________________")



class company_details:
    er = "-----------------------------------------------------------------------"
    company_name = "DELL PVT.LTD"
    company_reg_no = "MHT1102233CCC9443"
    def __init__(self,name,id):
        self.name = name
        self.id = id
        company_details.emp_address = "location - PUNE"
    def show(self,emp_blood_grp):
        print(company_details.er)
        company_details.age_limit = "25-55"
        self.blood_grp = emp_blood_grp
        print("company name :", company_details.company_name)
        print("company registered no :", company_details.company_reg_no   )
        print("employee_name:", self.name)
        print("employee id:",self.id)
        print("blood group :",self.blood_grp)
        print("age_limit:",company_details.age_limit)
        print("EMP ADDRESS:", company_details.emp_address)

obj = company_details("sangram",1011213)
company_details.payment_range = "25000-1500000"
obj.show("a+")
print("company payment range :" ,company_details.payment_range)
print("______________________________________________________________________________________________")



class static:
    company_name = "NICHROME INDIA PVT.LTD"
    company_reg_no = "MITRN1232433434334"
    def __init__(self,emp_name,emp_age):
        self.empname = emp_name
        self.age = emp_age
        static.location = "PUNE"

    def staticobj(self,blood_grp):
        self.emp_bloodgrp = blood_grp
        static.gender = "MALE"
        print("COMPANY NAME :",static.company_name)
        print("COMPANY REG. NO :",static.company_reg_no)
        print("EMPLOYEE NAME :",self.empname)
        print("EMPLOYEE AGE :",self.age)
        print("EMPLOYEE BLOOD GRP :",self.emp_bloodgrp)
        print("BRANCH :",static.location)
        print("GENDER :", static.gender)


onjstat = static("nitin jadhav",22)
static.AGE_LIMIT = "AGE LIMIT : 22-40"

onjstat.staticobj("O+")
print(static.AGE_LIMIT)
print("______________________________________________________________________________________________")



