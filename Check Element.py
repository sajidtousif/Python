my_set = {10, 20, 30, 40, 50}

element = int(input("Enter an element to check: "))

if element in my_set:
    print("Element", element, "is PRESENT in the set.")
else:
    print("Element", element, "is NOT PRESENT in the set.")
