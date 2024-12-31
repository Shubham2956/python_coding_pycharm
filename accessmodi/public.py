class public():
    a = "sameer"
    _b = "santosh"
    __c = "sagar"

    def show(self):
        print(public.a)
        print(public._b)
        print(public.__c)

class new_public(public):
    d = "naveen"
    e = "nayan"

    def show_1(self):
        print(public._b)
        print(new_public.d)
        print(new_public.e)


obj1 = new_public()
obj1.show_1()
obj = public()
obj.show()
print(obj._public__c)