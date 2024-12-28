import math
arr=[35,9,1,65,126,133]#list(map(int,input().split()))
count=0
for ele in arr:
    low=1
    high=math.ceil(ele**0.3)
    while low < high:
        res=low**3+high**3
        if res==ele:
            print("The good number is:",ele)
            count+=1
        if res<ele:
            low+=1
        else:high-=1
print(" count is:",count)