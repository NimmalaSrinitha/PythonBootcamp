def check(s):
    s.split()
    rev=''
    for i in s:
        rev=i+rev
    return rev
print(check('sri devi is engg college'))
'''


#reverse of words and sentence
def reverse(arr):
    rev=''
    for i in arr:
        rev=i+rev  
    return rev
arr=str(input())
print(reverse(arr))
'''

'''
def check(s):
    s = s.strip().split()  # Remove leading and trailing whitespace
    s = list(reversed(s))  # Reverse the list
    print(s)
    for i in s:
        rev = i[::-1]  # Reverse each word
        print(rev, end=' ')  # Print each reversed word with a space

s = input()
check(s)
'''