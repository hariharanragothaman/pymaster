import itertools
import operator
from itertools import accumulate, groupby


class Array:
    def sum_of_all_numbers(self, A):
        ans = list(accumulate(A, operator.add))
        return ans[-1]

    def product_of_all_numbers(self, A):
        ans = list(accumulate(A, operator.mul))
        return ans[-1]

    def consecutive_combinations_of_one(self, A):
        for x, y in zip(A, A[1:]):
            print(x, y)

    def consecutive_combinations_of_two(self, A):
        for x, y in zip(A, A[1:], A[2:]):
            print(x, y, x)

    def flatten_list(self, A):
        flat_list = [item for sublist in A for item in sublist]
        return flat_list

    def flatten_list2(self, A):
        flat_list = list(itertools.chain(*A))
        return flat_list

    def split_based_on_delimiter(self, A, delimiter):
        chunks = (list(g) for k, g in groupby(A, key=lambda x: x != delimiter) if k)
        result = [c for c in chunks]
        return result
