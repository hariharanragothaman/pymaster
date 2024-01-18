"""
Multiplying larger integers, when given as an array
"""


def multiply(num1, num2):
    # Smart way to get the sign
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    result = [0] * (len(num1) + len(num2))
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Removing the leading zero's
    # Nice use of next()
    result = result[
        next((i for i, x in enumerate(result) if x != 0), len(result)) :
    ] or [0]
    return [sign * result[0]] + result[1:]


if __name__ == "__main__":
    num1 = [1, 9, 3, 7, 0, 7, 7, 2, 1]
    num2 = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]
    res_value = multiply(num1, num2)
    print(res_value)
