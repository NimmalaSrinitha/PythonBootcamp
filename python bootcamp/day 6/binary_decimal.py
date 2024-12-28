#convert binary to decimal
def binary_decimal(n):
    sum=0
    i=0
    while n>0:
        rem=n%10
        pro=rem*pow(2,i)
        sum+=pro
        i+=1
        n=n//10
    print(sum)#43
n=int(input())#101011
binary_decimal(n)