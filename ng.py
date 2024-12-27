import random
print("---------->> hello ! wellcome in PARTH code in python to day i will give you 7 chance to guess number between 1 - 100 <<----------")
for i in range(7):
    a = int(input("enter your numer : "))

    guess_number = random.randrange(100)
    print(guess_number)
    
    if(a < guess_number):
        print("too low")
    elif(a > guess_number):
        print("too high")
    elif( a == guess_number):
        print("you win")
        break