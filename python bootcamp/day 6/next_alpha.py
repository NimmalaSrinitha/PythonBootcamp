# print the next alphabet
s="zabced"
for c in s:
    if ord(c)>=97 and ord(c)<122:
        print(chr(ord(c)+1),end=" ")
    else:
        print(chr(ord(c)-25),end=" ")