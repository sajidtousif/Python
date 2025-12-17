num = int(input("Enter a decimal number: "))

print("1) Binary")
print("2) Octal")
print("3) Hexadecimal")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Binary:", bin(num)[2:])
    case 2:
        print("Octal:", oct(num)[2:])
    case 3:
        print("Hexadecimal:", hex(num)[2:].upper())
    case _:
        print("Invalid Choice")
