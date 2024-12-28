from collections import deque
num=[1,2,3,4]
num=deque(num)
num.pop()
print(num)
num.popleft()
print(num)