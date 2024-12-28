#double pointer
arr=[4,1,5,3,2,6,7]#array should be in sorted order
k=8
count=0
f=0
l=len(arr)-1
arr=sorted(arr)
while f<l:
    if arr[f]+arr[l]==k:
        count+=1
        f+=1
        l-=1
    elif arr[f]+arr[l]<k:
        f+=1
    else:
        l-=1
print(count)