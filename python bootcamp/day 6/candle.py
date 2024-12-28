# to count how many 
candle=[3,7,1,5,4,7]
print(candle.count(max(candle)))#using buildin functions

count=0
max=candle[0]
for i in candle:
    if i>=max:
        max=i
for i in candle:
    if max==i:
        count+=1
print(count)