s=input()
s1=''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
if s==s1:
    print(s+ " is a palindrome")
else:
    print("not a palindrome")