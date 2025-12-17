numbers = []

print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

print("List =", numbers)
print("Smallest number =", min(numbers))
print("Largest number =", max(numbers))
