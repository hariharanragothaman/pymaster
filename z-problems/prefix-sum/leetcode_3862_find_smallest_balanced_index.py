class Solution:
    def smallestBalancedIndex(self, A: list[int]) -> int:
        n = len(A)
        PS = [0] * (n+1)
        for i in range(1, n+1):
            PS[i] = PS[i-1] + A[i-1]
        # print(PS)

        PP = [1] * (n+1)
        for i in range(n-1, -1, -1):
            PP[i] = PP[i+1] * A[i]

        for i in range(0, n):
            ls = PS[i] - PS[0]
            rs = PP[i+1]
            if ls == rp:
                return i
        
        return -1

if __name__ == "__main__":
    A = [2,1,2]
    print(Solution().smallestBalancedIndex(A))