ch = input("Enter an alphabet: ")

if 'a' <= ch <= 'z':
    ch = chr(ord(ch) - 32)
elif 'A' <= ch <= 'Z':
    ch = chr(ord(ch) + 32)

print("Opposite case:", ch)
