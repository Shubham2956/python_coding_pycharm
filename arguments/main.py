print("1.....example of positional arguments.....if we change the postion of the arguments while "
      "declaration it may get cause the issue so ....in the positional argument no of sequence of the "
      "argument is necessary ")
def add(name,address):
    print(name)
    print(address)

add("sahil","pune")


print("2....default argument ...it is the tehnique in which we already set the variable and its value while creation .."
      "default argument always declare in the last if we not provide any value then it will"
      "access its default value and if we give value other than the declare deault value then"
      "it will takes that value. ")
def defarg(EMP_NAME,emp_id,comp_name = "ibm"):

    print(EMP_NAME)
    print(emp_id)
    print(comp_name)

defarg("akash","ibm548583",)



print("3...variable lenght argument ....whenever we dont know that how many arguments to be passed so at that time "
      "we use variable length argument so that we can pass no . of values and it return all values"
      "")
def varlenarg(*args):
    print(args)

varlenarg(2,3,4,5,4,5,3,4,4,"SHUBHAM","SANTUL")


print("4....keyword argument is the technique in which we can access the variable "
      "by using its names ...whenever their are no. of variables declare in the function "
      "so in that condition for avoiding the changing value of variables we can directly "
      "call the variable by using its name and then can pass the value to it...")
def keyarg(nooftyre = 0, nameofcar='toyota' ,colorofcar = 'black', varient='diesel/petrol',costofthecar = 100000000 ):
    print(nooftyre)
    print(nameofcar)
    print(varient)
    print(colorofcar)
    print(costofthecar)

keyarg(colorofcar="dark red",nameofcar="toyota-innova",nooftyre=4,varient="diesel",costofthecar=2300000)



print("5...variable length keyword argument ...is the technique inb which we can give both name and value at the of the decalration of the function ")
def varlenkeyarg(**kwargs):
    print(kwargs)

varlenkeyarg(name="akash",emp_id = 101122,qualification = 'MCA' ,SALARY = 120000 )