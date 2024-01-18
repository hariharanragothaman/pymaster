import itertools


def flatten_list(A):
    flat_list = [item for sublist in A for item in sublist]
    return flat_list

def flatten_list2(A):
    flt = list(itertools.chain.from_iterable(A))
    return flt

if __name__ == '__main__':
    list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(flatten_list(list1))
    print(flatten_list2(list1))
