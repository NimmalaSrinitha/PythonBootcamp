import random
ran=random.randint(1,10)
count=0
chance=1
while chance<=3:
    guess=int(input())
    if guess==ran:
        print("congratulations")
        break
    else:
        chance+=1
        continue
if chance>3:
    print("failed to try next time")