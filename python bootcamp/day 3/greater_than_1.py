arr=list(map(int,input().split()))
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
for num,count in d.items():
    if count>1:
        print(num,end=" ")