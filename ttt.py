b = input("What to do (+, -, *, /): ")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if b == "+":
    print(num1 + num2)
elif b == "-":
    print(num1 - num2)
elif b == "*":
    print(num1 * num2)
elif b == "/":
    print(num1 / num2)
else:
    print("Wrong operation")
