# sum of integers in given input

s=input()
sum=0
count=0
for i in range(0,len(s)):
    if s[i].isdigit():  #it will check for the digits in given input
        sum+=int(s[i])
        count+=1
print(count)
print(sum)