class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sn = len(s)
        tn = len(t)

        cnt = 0
        for i in range(0, sn):
            if cnt < tn and s[i] == t[cnt]:
                cnt += 1

        ans = 0 if cnt == tn else tn - cnt
        return ans


if __name__ == '__main__':
    obj = Solution()
    s = "coaching"
    t = "coding"
    ans = obj.appendCharacters(s, t)
    print(ans)
    print(s[5])
