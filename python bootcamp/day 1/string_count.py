#count the number of string in a given input
n=input()
count=0
for i in n:
    if not(i.isdigit()):
        count+=1
print(count)