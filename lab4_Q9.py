#taking input
X=input("enter a sentence")
#initialization
upp=0
lower=0
dig=0
spec=0
ind=0
##looping
while ind<len(X):
    cha=X[ind]
    #conditions
    if 'A'<=cha<='Z':
        upp+=1
    elif 'a'<=cha<='z':
        lower+=1
    elif '0'<=cha<='9':
        dig+=1
    else:
        spec+=1 
    ind+=1   
#output      
print(upp)
print(lower) 
print(dig)
print(spec)