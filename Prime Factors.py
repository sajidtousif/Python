num = int(input("Enter a number: "))
n = num

print("Distinct Prime Factors are:", end=" ")

i = 2
distinct_factors = set()

while i * i <= n:
    while n % i == 0:
        distinct_factors.add(i)
        n //= i
    i += 1

if n > 1:
    distinct_factors.add(n)

print(", ".join(str(x) for x in sorted(distinct_factors)))
