from typing import List


class Solution:
    def carPooling(self, A: List[List[int]], capacity: int) -> bool:
        A = sorted(A, key=lambda x:x[1])
        intervals = []

        for p, s, e in A:
            intervals.append((s, p))
            intervals.append((e, -p))

        sweep = sorted(intervals)
        print(sweep)

        total = 0
        for pos, ppl in sweep:
            if total + ppl <= capacity:
                total += ppl
            else:
                return False
        return True


if __name__ == '__main__':
    # Return the minimum number of conference rooms required
    trips = [[2,1,5],[3,3,7]]
    s = Solution()
    res = s.carPooling(trips, capacity=4)
    print(res)