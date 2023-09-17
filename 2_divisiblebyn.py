#

X = int(input("Enter Number 1 :"))  #Enter intial number
Y = int(input("Enter Number 2 :"))  #Enter final number
N = int(input("Enter the number to check divisibility : ")) #Enter divident

count = X+1 #Initialize count to step up the num
while count<Y:
    if N%count==0:  #Check divisibility
        print(count)    #Display divisible number
        count=count+1   #If divisible step up by 1
    else:
        count=count+1   #If not divisible step up by 1
    