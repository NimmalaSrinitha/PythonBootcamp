'''
s=input()
count=0
for i in range(0,len(s)):
    vowels='aAeEiIoOuU' 
    if s[i] in vowels:
        count+=1
print(count)
'''
#LIST without range
s=input()
count=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in vowels:
        count+=1
print(count)
