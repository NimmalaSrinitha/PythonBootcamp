import random
ran=random.randint(1,10)
while True:
    guess=int(input())
    if guess==ran:
        print("congratulations")
        break
    else:
        continue
print("failed to try next time")