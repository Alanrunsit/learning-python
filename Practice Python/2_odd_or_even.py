number=int(input("Enter a number: "))
check=int(input("Enter a numebr to divide by: "))

if number%4==0:
    print("The number is a multiple of 4.")
elif number%2==0:
    print("The number is even.")
else:    
    print("The number is odd.")

if number % check == 0:
    print("This number is evenly divided by ",check)
else:
    print("This number is not evenly divided by ",check)