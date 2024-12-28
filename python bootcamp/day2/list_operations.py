# list operations
mob=['vivo','oppo','samsung','iphone','motorola']
mob.insert(2,'oneplus')
print(mob)
mob.append('realme')
print(mob)
mob.remove('motorola')
print(mob)
mob.pop(-1)
print(mob)
mob[3]='redme'
print(mob)
print(mob[True])#means 1
print(mob[not True])#means 0
mob.clear()
print(mob)