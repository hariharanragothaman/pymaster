from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0

        line_sweep = []

        for s, e in intervals:
            line_sweep.append((s, 1))
            line_sweep.append((e, -1))

        line_sweep = sorted(line_sweep)
        print(line_sweep)
        cnt = 0
        for f, s in line_sweep:
            cnt += s
            rooms = max(cnt, rooms)
        return rooms


if __name__ == '__main__':
    # Return the minimum number of conference rooms required
    intervals = [[0,30],[5,10],[15,20]]
    s = Solution()
    res = s.minMeetingRooms(intervals)
    print(res)