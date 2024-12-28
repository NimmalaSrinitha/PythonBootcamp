def fib(n):
    t1=0
    t2=1
    print(t1,t2,end=' ')
    count=0
    while count<n:
        t3=t1+t2
        print(t3,end=' ')
        t1=t2
        t2=t3
        count+=1
n=int(input())
fib(5)
