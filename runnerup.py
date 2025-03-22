user_input = input("enter element by space ").split()
print(user_input)
print(type(user_input))

user_list = [int(i) for i in user_input]
print("the list is :",user_list)
user_list.sort()
print("sorted list is :",user_list)
print("second largest number is ",user_list[-2])
print("second smallest number is ",user_list[1])
