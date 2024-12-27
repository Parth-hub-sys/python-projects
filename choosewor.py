# import random

# name = input("What is your name? ")

# print("Good Luck ! ", name)

# words = ['rainbow', 'computer', 'science', 'programming',
#          'python', 'mathematics', 'player', 'condition',
#          'reverse', 'water', 'board', 'geeks']

# word = random.choice(words)

# print("Guess the characters")

# guesses = ''
# turns = 12

# while turns > 0:

#     failed = 0

#     for char in word:

#         if char in guesses:
#             print(char, end=" ")

#         else:
#             print("_")
#             failed += 1

#     if failed == 0:
#         print("You Win")
#         print("The word is: ", word)
#         break

#     print()
#     guess = input("guess a character:")

#     guesses += guess

#     if guess not in word:

#         turns -= 1
#         print("Wrong")
#         print("You have", + turns, 'more guesses')

#         if turns == 0:
#             print("You Loose")

import random

name = input("hey ! what is your name : ")
print("good luck ",name)

key = ['winter','kingslanding','bararhiyan','berline','surat','tokyo','jawa42','duke390']
word = random.choice(key)


print("guess the name below list")
print(key)

chances = 3
while chances > 0:
    print("you have", chances, "chances left")
    guess = input("guess the word ---------->> ")
    if guess == word:
        print("you win")
        break
    else:
        print("you loose")
        chances = chances - 1
        
print("random choise is "+word)