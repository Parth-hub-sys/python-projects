import random

def game(com,user):
    if(com == user):
        print("drow match")
    elif(com == 1 and user == 2):
        print("you lose")
    elif(com == 2 and user == 3):
        print("you lose")
    elif(com == 3 and user == 1):
        print("you lose")
    else:
        print("you win")

print("do you want to play \n 1.ketchi\n 2.PAPPER \n 3.punch ")


user = int(input("enter a number "))
com = random.randint(1,3)

if user > 3 or user < 1:
    print("please enter valid input range 1-3")
    
    
game(com,user)
print("your choise is a ",user)
print("computer choise is a ",com)


        

