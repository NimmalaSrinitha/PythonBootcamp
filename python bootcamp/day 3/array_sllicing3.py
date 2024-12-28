arr=[1,2,3,4,5,6]
k=int(input())
second=arr[k+2:k:-1]# for last 2 elements
first=arr[:k+1]#upto k elements
print(first)
print(second)
print(second+first)
