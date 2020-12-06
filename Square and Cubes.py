#display square and cube of first n(given by user) natural numbers
x = int(input("Enter Desired Valure:-"))
for x in range (0,x+1):
    square = x**2
    cube = x**3
    print("The square of",x,"is",square,"and cube is",cube)
