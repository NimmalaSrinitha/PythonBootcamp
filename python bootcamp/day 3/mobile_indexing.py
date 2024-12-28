#getting data from even index
mob=['vivo','oppo','samsung','iphone','motorola']
m=1
rev=[]
for i in range(0,len(mob)):
    if i%2==0:
        rev=mob[i]#to get the elements in reverse
        #print(m,mob[i])
        print(rev[::-1])
        m+=1