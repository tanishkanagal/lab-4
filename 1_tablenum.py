#Make a table of a number

num = int(input("Enter the number to make a multiplecation table : ")) #Enter number to make table
count = 1   #Initialze count
if num>=0:
    while count<=20: #Count till 20
        print(num,"x",count,"=",num*count)  #Print table
        count+=1
else:
    print("Invalid Input")