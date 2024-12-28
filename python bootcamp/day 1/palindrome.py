#palindrome between 1-50
def check(n):
    n=str(n)
    return len(n)>1 and n==n[::-1]
def increment(N):
    count=0
    for i in range(1,N+1):
        if check(i):
            print(i)
            count+=1
    return count
N=50
print(increment(N))
