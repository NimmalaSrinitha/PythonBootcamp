try:
    a=10
    b=0
    c=a/b
    print(c)
    n1=100
    n2=200
    print(n1+n2)# exception occured so the next lines are not executed
except Exception:
    print("divided by zero is not valid")
    n1=100
    n2=200
    print(n1+n2)
    a1=1000
    a2=2000
    print(a1+a2)