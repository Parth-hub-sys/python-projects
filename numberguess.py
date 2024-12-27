# import random

# #this programme as well as can use a 4-digit  password creaker 


# n = str(random.randrange(1000, 10000))  # convert n to a string
# e = [int(digit) for digit in n]  # create a list of individual digits
# print(n)

# p = input("enter a 4 digit number : ")
# if(len(p)<4 or len(p)>4):
#     print("please enter 4 digit number")
# else:
#     print("you entered a 4 digit number")
#     print("let's check........")
#     o = [int(d) for d in p]
#     print(o)
    
#     for i in range(4):
#         for j in range(4):
#             if o[i] == e[j]:
#                 print(f" number contain positin {j+1} digit {o[i]}")
           

#     for i in range(4):
#         if o[i] == e[i]:
#             print(f"Match found at position {i+1} with digit {o[i]}")
            
#         else:
#             print(f"No match found at position {i+1} with digit {o[i]}")
            
            
# print(n)
    
# import random

# #this programme as well as can use a 4-digit  password creaker 


# n = str(random.randrange(1000, 10000))  # convert n to a string
# e = [int(digit) for digit in n]  # create a list of individual digits
# print(n)

# p = input("enter a 4 digit number : ")
# if(len(p)<4 or len(p)>4):
#     print("please enter 4 digit number")
# else:
#     print("you entered a 4 digit number")
#     print("let's check........")
#     o = [int(d) for d in p]
#     print(o)
    
#     result = []  # create an empty list to store the result
    
#     for i in range(4):
#         for j in range(4):
#             if o[i] == e[j]:
#                 result.append(o[j])  # append the matched digit to the result list
#                 print(f"Match found at position {j+1} with digit {o[i]}")
       
#             result.append("-")  # append "-" to the result list for non-matched digits
#                 # print(f"No match found at position {i+1} with digit {o[i]}")
            
#     print("Result:", result)
    
            
            
        
            
import random

# This program can be used as a 4-digit password cracker

n = str(random.randrange(1000, 10000))  # convert n to a string
e = [int(digit) for digit in n]  # create a list of individual digits
print(n)

p = input("Enter a 4-digit number: ")
if len(p) < 4 or len(p) > 4:
    print("Please enter a 4-digit number")
else:
    print("You entered a 4-digit number")
    print("Let's check........")
    o = [int(d) for d in p]
    print(o)

    match_result = ["-"] * 4  # Initialize a list to store match results

    for i in range(4):
        for j in range(4):
            if o[i] == e[j]:
                print(f"Number contains position {j+1} digit {o[i]}")

    for i in range(4):
        if o[i] == e[i]:
            print(f"Match found at position {i+1} with digit {o[i]}")
            match_result[i] = f"{o[i]} (Match)"  # Update the match result list
        else:
            print(f"No match found at position {i+1} with digit {o[i]}")
            match_result[i] = f"{o[i]} (No Match)"  # Update the match result list

    print("\nMatch Results:")
    for i, result in enumerate(match_result):
        print(f"Position {i+1}: {result}")

print(n)