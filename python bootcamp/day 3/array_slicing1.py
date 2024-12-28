#slicing in list
arr=[1,2,3,4,5,6]
k=int(input())
first=arr[:k-1]# it gives the first part data upto k
second=arr[k-1:]# it gives the second part data from k
print(first)
print(second)
print(second+first)# it will display second part with first part
first.extend(second)# it connect the second part with first part
print(first)