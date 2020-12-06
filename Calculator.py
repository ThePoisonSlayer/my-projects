print("\n\n\n\n\t\t\t\t\tCALCULATOR\n\n\n")

x = int(input("Enter the first number:-"))
y = int(input("Enter the second number:-"))

print("\n\nThere are 7 options\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Reminder of Division\n6.Powers")
for a in range(0,65500):
    z = int(input("\n\nChoose an option:-"))
    if z<7 and z>0:
        if z==1:
            print("\nThe option you chose is Addition\n")
            print(x,"added to",y,"is",x+y)
        elif z==2:
            print("\nThe option you chose is Subtraction\n")
            print(y,"subtracted from",x,"is",x-y)
        elif z==3:
            print("\nThe option you chose is Multiplication\n")
            print(x,"multiplied by",y,"is",x*y)
        elif z==4:
            print("\nThe option you chose is Division\n")
            print(x,"divided by",y,"is",x/y)
        elif z==5:
            print("\nThe option you chose is Remainder Checking\n")
            print("The remainder",x%y,"remains when you divide",x,"by",y)
        elif z==6:
            print("\nThe option you chose is Exponents\n")
            print(x,"to the power of",y,"is",x**y)
    else:
        print("Choose an option from the given choices!!")

print("\n\n\n\n\nEpic Calculations Procedure developed by Pratham Virani")
