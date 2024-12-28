n1=2545
n2=5478
carry=0
count=0
while n1>0 and n2>0:
    rem1=n1%10
    rem2=n2%10
    sum=rem1+rem2+carry
    if (sum>9):
        carry=1
        count+=1
    else:
        carry=0

    n1=n1//10
    n2=n2//10
    print(sum,carry)# to get the each sum and carry
print(count)