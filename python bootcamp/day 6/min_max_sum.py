num=[1,2,3,4,5,6]
num.sort()
min_sum=sum(num[:len(num)-1])
max_sum=sum(num[1:])
diff=abs(min_sum-max_sum)
print(min_sum,max_sum,diff)