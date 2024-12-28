'''
try:
    a=5
    print(b)
except NameError:
    print("Variables are not declared")

'''
try:
    arr=[1,2,3,4,5]
    print(arr[8])
except NameError:
    print("can't access the index values")
else:
    print("no exception occured")
finally:
    print("if exception occured also it will execute")