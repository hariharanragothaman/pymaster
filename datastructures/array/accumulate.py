from itertools import accumulate
import operator


def get_sum_of_all_numbers(A):
    ans = list(accumulate(A, operator.add))
    return ans[-1]

def get_product_of_all_numbers(A):
    ans = list(accumulate(A, operator.mul))
    return ans[-1]


if __name__ == '__main__':
    A = list(range(1, 6))
    print(get_product_of_all_numbers(A))
    print(get_sum_of_all_numbers(A))
