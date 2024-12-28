
def sum_single_digit(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    print(num)

# Example usage
num=int(input())
sum_single_digit(num)
