# Reversing an integer
def reverse_integer(num):
    sign = -1 if num < 0 else 1
    result = 0
    x = abs(num)

    while x:
        # Getting the LSB-  multiply by 10 every time;
        # since it will be correct as we add digits
        result = (x % 10) + result * 10
        # Remove the LSB
        x = x // 10

    # Handle overflow bound scenario
    if x > 2**31 + 1 or x < -(2**31) - 1:
        return 0

    return result * sign
