#Palindrome checker

num = int(input("Enter the number to check Palindrome : "))
rev = 0
temp = num

while temp>0:
    rem = temp%10
    rev = (rev*10) + rem
    temp=temp//10

if num==rev:
    print("It is a Palindrome")
else:
    print("Number is not a Palindrome")