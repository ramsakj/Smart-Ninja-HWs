first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
oper = input("Enter operation: ")

if oper == "+":
    print(first + second)
elif oper == "-":
    print(first - second)
elif oper == "*":
    print(first * second)
elif oper == "/":
    print(first / second)
else:
    print("I don't recognize this operation.")