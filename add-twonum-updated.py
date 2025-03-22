l1 = [2, 4, 3]  # Represents the number 342
l2 = [5, 6, 4]  # Represents the number 465

result = []
carry = 0

# Iterate through both lists
for i in range(max(len(l1), len(l2))):
    digit1 = l1[i] if i < len(l1) else 0
    digit2 = l2[i] if i < len(l2) else 0
    total = digit1 + digit2 + carry
    result.append(total % 10)  # Append the last digit of the total
    carry = total // 10  # Update carry

if carry:
    result.append(carry)  # Append any remaining carry

print(result)  # Output the result
