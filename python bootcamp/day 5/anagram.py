#length should be same and same characters
s1='tab'
s2='bata'
for i in s1:
        if len(s1)==len(s2) and i in s2:
            print("anagram")
            break
        else:
            print("not anagram")
            break

'''
s1='tab'
s2='bata'
res1=sorted(s1)
res2=sorted(s2)
if len(21)==len(s2) and res1==res2:
    print("anagram")
else:
    print("not an anagram")
'''