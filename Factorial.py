#display factorial of numbers
a = 1
x = int(input("Enter a number:-"))
for y in range (1,x+1):
    a *= y
print ("The factorial of",x,"is",a)
