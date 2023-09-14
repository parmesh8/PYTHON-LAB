#taking input
num = int(input("Enter a number:"))  
#initialization variables
i = 2
f=0
#checking
if num<0:
    print("invalid input")
if num==1:
    print("1 is neither prime nor composite")
##looping
while i <= num:
    if num % i == 0:
        f=1  
    break
if f==1:
    print("The entered number is not a  PRIME number")
else:
    print("The entered number is  a PRIME number")
i=i+1

   
