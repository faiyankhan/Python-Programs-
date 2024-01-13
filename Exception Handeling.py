# Exception Handeling in Python .
try:   
    a = int(input("Enter your Number: "))
    print(a+10)
except Exception as e:
     print("some error occurred: ",e)

a = input("Enter the Number: ")
print(f"Multiplication table of {a} is: ")

for i in range(1,11):
     print(f"{int(a)} X {i} = {int(a)*i}") 

print("Some Imp lines of Code")
print("End of Program")

try:
     num = int(input("Enter an intiger: "))
     a = [5,5]
     print(a[num])
except ValueError:
     print("Number entered is not an integer.")

except IndexError:
     print("Index Error")