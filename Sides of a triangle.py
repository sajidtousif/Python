a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

# a + b > c  AND  a + c > b  AND  b + c > a
result = int((a + b > c) and (a + c > b) and (b + c > a))

print("Output:", result)
