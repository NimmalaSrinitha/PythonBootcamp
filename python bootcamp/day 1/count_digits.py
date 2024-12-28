#check for integer in given input
s=input()
count=0
for i in range(0,len(s)):
    if s[i].isdigit():  #it will check for the digits in given input
        count+=1
print(count)
