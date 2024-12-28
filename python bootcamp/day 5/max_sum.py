n1=4378
n2=6273
n3=2354
def min_check(n):
    s=str(n)
    min=int(s[0])
    for i in s:
        if int(i) < min:
            min=int(i)
    return min
def max_check(n):
    s=str(n)
    max=int(s[0])
    for i in s:
        if int(i)>max:
            max=int(i)
    return max
min_sum=min_check(n1)+min_check(n2)+min_check(n3)
max_sum=max_check(n1)+max_check(n2)+max_check(n3)
diff=abs(min_sum-max_sum)
print(diff)
