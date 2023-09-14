n=int(input("Enter a   number:"))
temp=n
re=0
while(n>0):
    dig=n%10
    re=(re*10)+dig
    n=n//10
if(temp==re):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")