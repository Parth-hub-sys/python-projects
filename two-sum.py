
a = [12, 13, 14, 15]
print(a)

target = 30

for i in range(len(a)):
    for j in range(len(a)): # This is inefficient
        if a[i] + a[j] == target:
            print(f"Found: {a[i]} (index {i}) + {a[j]} (index {j}) = {target}")
            break
        else:
            print(f"Did not find: {a[i]} + {a[j]} = {target}")

