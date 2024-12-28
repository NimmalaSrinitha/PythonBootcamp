n=1729
s=0
prod=1
while(n>0):
    d=n%10
    prod=prod*d
    n=n//10
print(prod)