class PrefixSum:
    @staticmethod
    def get_prefix_sum(self, A):
        n = len(A)
        PS = [0] * (n + 1)
        for i in range(1, n + 1):
            PS[i] = PS[i - 1] + A[i - 1]
        print("The prefix sum array is:", PS)
        return PS

    @staticmethod
    def get_sum(self, A, l, r):
        total = 0
        for i in range(l, r + 1):
            total += A[i]
        return total





if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
