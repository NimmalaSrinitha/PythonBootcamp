'''
task2
count halindrome
s=['aba','sasdad','aaaccc']
if not a palindrome then divide the string 
if any one of the part is palindrome then it is a halindrome
'''
s = ["aba", "sasdad", "aaaccc", "tapdog","emepe"]
count = 0

for i in s:
    if i==i[::-1]:
        count+=1
    else:
        m=len(i)//2
        if len(i)%2==0:
            first=i[:m]
            second=i[m:]
            if first==first[::-1] or second==second[::-1]:
                count+=1
            print(i)               
        else:
            first=i[:m+1]
            second=i[m+1:]
            if first==first[::-1] or second==second[::-1]:
                count+=1
            print(i)
print(count)