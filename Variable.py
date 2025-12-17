#Q.1) Assign different types of values to different variables, print them and display all the
#variables which you have created. Then display the types of all variables and delete a
#particular variable.
a = 10                     
b = 3.14                   
c = "Hello, Python!"       
d = True                   
e = [1, 2, 3]              
f = (4, 5, 6)              
g = {"name": "Sajid"}      

print("Values of variables:")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

print("\nTypes of variables:")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

del c

print("\nVariables after deleting 'c':")
print(a, b, d, e, f, g)
