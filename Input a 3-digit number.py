num = int(input("Enter a 3-digit number: "))

hundreds = num // 100            
tens = (num // 10) % 10          
ones = num % 10                 

reverse_num = (ones * 100) + (tens * 10) + hundreds

print("Reverse of the number is:", reverse_num)
