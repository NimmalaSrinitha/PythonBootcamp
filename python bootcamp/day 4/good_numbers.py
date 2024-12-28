import math
arr=[35,9,1,65,126,133]#list(map(int,input().split()))
count=0
for ele in arr:
    low=1
    high=math.ceil(ele**0.3)
    while low < high:
        res=low**3+high**3
        if res==ele:
            print(ele)
            count+=1
        low+=1
print(" count is:",count)