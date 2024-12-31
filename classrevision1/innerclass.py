class main:
    def __init__(self):
        print("this is main class")
    class inner:
        def __init__(self):
            print("this is inner class")
        def show(self):
            print("this is the innermost class")

obj = main()
obj.inner()
e = main().inner().show()




