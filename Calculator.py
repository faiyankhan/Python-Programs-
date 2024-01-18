# Calculatro using Python .
first = input("Enter First Number:")
operator = input("Enter Operator (+,-,*,/,%) :")
Second = input("Enter second Number: ")

first = int(first)
Second = int(Second)
if operator == "+":
    print(first + Second)
if operator == "-":
    print(first - Second)
elif operator == "*":
    print(first * Second)
elif operator == "/":
    print(first / Second)
elif operator == "%":
    print(first % Second)
else:
    print("Invalid operator")