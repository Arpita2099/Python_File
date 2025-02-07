# How to make a project of Rock paper and Scissor by using Random modul in python:
'''
Winning Rules as follows:
Rock Vs Paper: Paper will win.
Rock Vs Scissor: Rock will win.
Paper Vs Scissor: Scissor will win.
'''

import random
l=["Rock","Scissor","Paper"]

while True:
    Ccount=0
    Ucount=0
    User_Choice=int(input('''
    Game Start......
    1 Yes
    2 No | Exit
    '''))
    if User_Choice==1:
        for a in range(1, 6):  # Loop to allow 5 rounds of the game
            User_Input = int(input('''
                       1 Rock
                       2 Scissor
                       3 Paper
                       '''))
            if User_Input==1:
                uchoice="Rock"
            elif User_Input==2:
                uchoice="Scissor"
            elif User_Input==3:
                uchoice="Paper"

            Computer_choice= random.choice(l)
            if Computer_choice==uchoice:
                print("Computer Value",Computer_choice)
                print("User Value",uchoice)
                print("Game Draw")
                Ucount=Ucount+1
                Ccount=Ccount+1
            elif((uchoice=="Rock" and Computer_choice=="Scissor") or (uchoice=="Paper" and Computer_choice=="Rock") or (uchoice=="Scissor" and Computer_choice=="Paper")):
                print("You Win this Round")
                Ucount=Ucount+1
            else:
                print("Computer Value",Computer_choice)
                print("User Choice",uchoice)
                print("Computer Win this Round")
                Ccount=Ccount+1

        if Ucount==Ccount:
            print("Final Game Draw.....")
            print("User Score",Ucount)
            print("Computer Score",Ccount)
        elif Ucount>Ccount:
            print("You Win the Game.")
            print("User Score", Ucount)
            print("Computer Score", Ccount)
        else:
            print("Computer Win the Game")
            print("User Score", Ucount)
            print("Computer Score", Ccount)

    else:
        break
