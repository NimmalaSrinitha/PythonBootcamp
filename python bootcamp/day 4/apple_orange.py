s=7
t=11
a=3
b=15
a1,b1=0,0
apples=[6,5,-4]
oranges=[9,8,-4]
for i in apples:
    if a+i>=s and a+i<=t:
        a1+=1
print("number of apples at sam house",a1)
for i in oranges:
    if b+i>=s and b+i<=t:
        b1+=1
print("number of oranges at sams house",b1)
print("total apples and oranges",a1+b1)


#
'''
for i in apples:
    if a+i in range(a,t+1):
        a1+=1
for i in oranges:
    if b+i in range(s,t+1):
        b1+=1
print(a1,b1)
'''