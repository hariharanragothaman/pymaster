class Solution:
    def solve(self, n):
        op = [[1], [1, 1]]
        if n == 0:
            return op[0]
        elif n == 1:
            return op[1]
        i = 2
        while i < n:
            candidate = op[-1]
            temp = []
            for i in range(1, len(candidate)):
                temp.append(candidate[i] + candidate[i - 1])
            temp = [1] + temp + [1]
            op.append(temp)

            i += 1
        return op[-1]


# Another way of doing is as follows:
# We can build the final answer immediately, using the identity binom(n, i) = binom(n, i - 1) * (n - i + 1) // i.

class Solution:
    def solve(self, n):
        ans = [1]
        for i in range(1, n + 1):
            ans.append(ans[-1] * (n - i + 1) // i)
        return ans
