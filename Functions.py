# Functions in Python .
def greetHello(Name , Ending):
    print("Hello " + Name)    
    print("Hello")
    print("Hello")
    print("Hello")
    print(Ending)

def letterGenerator(Name , Date):
    st = f"Hii mam , This is {Name} and I will Not come to school on {Date}"
    print(st)

def average(a,b):
    return (a+b)/2

print("Executing function ...")
greetHello("Faiyan khan ", "Thank you")
greetHello("Abhishek Mandal", "Thank you")
letterGenerator("Faiyan khan ","15 January")
letterGenerator("Abhishek Mandal","18 January")
print(average(40,60))
print("Done")