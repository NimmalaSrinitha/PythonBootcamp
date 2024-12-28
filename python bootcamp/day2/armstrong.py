# check whether the given number is armstrong number or not
def is_armstrong(num):
    original_num = num
    sum_of_cubes = 0   
    while num > 0:
        d = num % 10
        sum_of_cubes += d ** len(str(original_num))
        num //= 10
    
    if original_num == sum_of_cubes:
        return "it is armstrong"
num=int(input())
print(is_armstrong(num))

