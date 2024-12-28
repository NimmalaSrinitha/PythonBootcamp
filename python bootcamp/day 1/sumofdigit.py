n=1729
s=0
rev=0
prod=0
while(n>0):
    d=n%10
    s=s+d
    n=n//10
    rev=rev*10+d
print(s)#sum of digits in input
print(rev)# reverse of input
