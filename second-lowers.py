# Number of entries to be input
n = int(input("How many students' data do you want to enter? "))

# Create an empty list to store the data
data = []

# Take input for each student
for _ in range(n):
    name = input("Enter the student's name: ")
    marks = int(input(f"Enter marks for {name}: "))
    data.append([name, marks])

# Sort the list by the second element (marks)
data.sort(key=lambda x: x[1])

# Print the sorted list
print("Sorted data:", data)

# Print the second lowest marks (second element of the second lowest entry)
print("Second lowest marks are:", data[1])  # This works if there are at least two entries
# Print the second highest marks (second element of the second highest entry)
print("Second highest marks are:", data[-2])  # This works if there are at least two entries