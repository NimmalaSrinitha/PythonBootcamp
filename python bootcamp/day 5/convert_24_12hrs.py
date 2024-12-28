time=input()
time=time.split(':')
hrs=time[0]
minutes=time[1]
sec=time[2]
if int(hrs)>12:
    hrs=int(hrs)-12

if int(minutes)>59:
    hrs=int(hrs)+1
    minutes=int(minutes)-60
    minutes=0
    
if int(sec)>59:
    minutes=int(minutes)+1
    sec=int(sec)-60
    sec=0
print(str(hrs)+":"+str(minutes)+":"+str(sec))