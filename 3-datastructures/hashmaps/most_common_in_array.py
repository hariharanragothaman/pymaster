from collections import Counter

def most_common_in_array(A):
    ctr = Counter(A)
    top_three_frequent = ctr.most_common(3)
    return top_three_frequent

if __name__ == '__main__':
    array = [1, 3, 5, 6, 7, 7, 1, 1, 2, 3]
    print(most_common_in_array(array))
