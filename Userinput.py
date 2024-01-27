# Userinput method in python.

name = input("Enter your Name: ")
print(type(name))
print(name)

# Write a python program to take a number from user as a input from the User and add 6 to it .
num = input("Enter a number: ")
print(type(num))
print(int(num) + 5)

# Combution of Two Numbers.
x = int(input("Enter first Number: "))
y = int(input("Enter Second Number: "))
print(x+y)

a = int(input("Enter A :"))
b = int(input("Enter B :"))
c = int(input("Enter C :"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
p = a+b+c
print("Area =",area)
print("perimeter =",p)

