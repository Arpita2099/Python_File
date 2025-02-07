# How to make calculator in python.
print('''
+ Add
- Subtract
* Multiply
/ Divide
''')
num1=int(input("Enter the first value: "))
num2=int(input("Enter the second value: "))
opr=input("Enter any operator...(+,-,*,/): ")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("Invalid value.")