# How to make a number guessing Game by using python randon module:

import random
Computer_Number=random.randrange(1,101)
User_Input=int(input("Enter Your Number----"))

if User_Input>Computer_Number:
    print("Computer Number is:-",Computer_Number)
    print("Your guess number is too high.")
elif Computer_Number>User_Input:
    print("Computer Number is:-", Computer_Number)
    print("Your guess number is too low.")
else:
    print("Computer Number is:-", Computer_Number)
    print("Your guess number is qual to computer number.")