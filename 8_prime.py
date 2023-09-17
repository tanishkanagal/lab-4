num = int(input("Enter the number to check for prime number : "))
count = 2
if num>1:
    while count<(num/2):
        if num%count==0:
            print("Not a prime number.")
            break
        count+=count
    else:
        print("It is a prime number")
elif num<0:
    print("Invalid Input")
else:
    print("Neither Prime nor Composite")