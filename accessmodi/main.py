class n1():
    id = 101
    _name = "keshav"
    __payment = 100000

    def show(self):
        print(n1.id)
        print(n1._name)
        print(n1.__payment)


obj = n1()
obj.show()
print(n1.id)
print(n1._name)
print(obj._n1__payment)

