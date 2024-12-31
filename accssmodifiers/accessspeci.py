# access specifiers or modifiers

### a = 101 -------public
### _a = 101 -------private
### __a = 101 -------protected



class new:
    a = 101
    _b = "sumit"
    __c = "+91-34434324"
    def n1(self):
        print(new.a)
        print(new._b)
        print(new.__c)

obj = new()
obj.n1()

print(new.a)
print(new._b)
print(obj._new__c)  #name mangling