a = 25
b = 10

print("Value of a:", a)
print("Value of b:", b)

print("Memory location of a:", id(a))
print("Memory location of b:", id(b))

print("Does 'a' and 'b' have same memory location?", id(a) == id(b))

float_div = a / b
print("Floating point division (a / b):", float_div)

int_div = a // b
print("Integer division (a // b):", int_div)
