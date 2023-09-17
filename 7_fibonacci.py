#Fibonacci Sequence

a = 1   #Predefined first term
b = 1   #Predefined second term
print(a)       
print(b)
temp=0
while (a+b)<1000:
    temp = a+b  #Sum of last 2 terms
    print(temp) #Print the last term
    a=b #reassign a==b 
    b=temp  #reassign b=temp