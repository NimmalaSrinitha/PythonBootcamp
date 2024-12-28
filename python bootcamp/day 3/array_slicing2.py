arr=[1,2,3,4,5,6]
k=int(input())
second=arr[k+2:k-1:-1]# for last 2 elements
first=arr[:k+1]
print(first) #first part upto k
print(second)# second part from reverse
print(second+first)
