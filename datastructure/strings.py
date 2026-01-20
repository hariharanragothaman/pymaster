import bisect
from collections import Counter
from difflib import SequenceMatcher

class Strings:

    def alpha_map_count(self):
        alpha = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        num = list(range(1, 27))
        return dict(zip(alpha, num))

    def alpha_map_bool(self):
        alpha = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        boolean = [False] * 26
        return dict(zip(alpha, boolean))

    def check_anagrams(self, S1, S2):
        ctr1 = Counter(S1)
        ctr2 = Counter(S2)
        return ctr1 == ctr2

    def check_anagrams_version2(str1, str2):
        hmap1 = [0] * 26
        hmap2 = [0] * 26

        for char in str1:
            pos = ord(char) - ord("a")
            hmap1[pos] += 1

        for char in str2:
            pos = ord(char) - ord("a")
            hmap2[pos] += 1

        return hmap1 == hmap2

class Palindromes:
    def is_palindrome(self, s):
        return s == s[::-1]

    def check_if_palindrome_can_be_formed(self, s):
        return sum(v % 2 == 1 for v in Counter(s).values()) <= 1

    def reorder_string_to_form_palindrome(self, s):
        n = len(s)
        ctr = Counter(s)
        ctr = {k: v for k, v in sorted(ctr.items(), key=lambda x: x[1], reverse=True)}

        # If there is more than one odd value in the count of letters - palindrome cannot be formed
        odd_count = 0
        for v in ctr.values():
            if v & 1:
                odd_count += 1
        if odd_count > 1:
            return "NO SOLUTION"

        # now going individually for odd and even cases
        if n & 1:
            # The length of the string is odd
            op = pivot = ""
            middle = ""

            # Finding the pivot:
            for k, v in ctr.items():
                if v % 2 != 0:
                    middle = k * v
                    pivot = k

            for k, v in ctr.items():
                if k != pivot:
                    op += k * (v // 2)
            return op + middle + op[::-1]

        else:
            # The length of the string is even
            op = ""
            for k, v in ctr.items():
                op += k * (v // 2)
            return op + op[::-1]

    def get_longest_palindrome_substring(self, s):
        lps = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(lps) > j - i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    lps = s[i:j]
                    break
        return lps

    def get_palindrome_from_string(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    def get_longest_palindrome_substring_optimized(self, s):
        lps = ""
        for i in range(len(s)):
            even = self.get_palindrome_from_string(s, i, i + 1)
            odd = self.get_palindrome_from_string(s, i, i)
            lps = max([lps, even, odd], key=lambda x: len(x))
        return lps


    # best Case algorithm
    def manachers_algorithm(self, s):
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = "#".join("^{}$".format(s))
        n = len(T)
        LPS = [0] * n
        C = R = 0

        for i in range(1, n - 1):
            LPS[i] = (R > i) and min(R - i, LPS[2 * C - i])  # equals to i' = C - (i-C)

            # Attempt to expand palindrome centered around i
            while T[i + 1 + LPS[i]] == T[i - 1 - LPS[i]]:
                LPS[i] += 1

            # if Palindrome centered around i expand past R,
            # adjust center based on expanded palindrome
            if i + LPS[i] > R:
                C, R = i, i + LPS[i]

        # Find max element in LPS
        max_length, center_index = max((n, i) for i, n in enumerate(LPS))
        return s[(center_index - max_length) // 2 : (center_index + max_length) // 2]

class Subsequences:
    def is_sub_sequence1(s, t):
        # Check if 's' is a subsequence of 't'
        for i in range(len(s)):
            try:
                index = t.index(s[i])
            except ValueError:
                return False
            t = t[index + 1 :]
        return True

    def is_sub_sequence2(s, t):
        # Check if 's' is a subsequence of 't'
        t = iter(t)
        return all(c in t for c in s)

    def longest_increasing_subsequence(arr):
        temp = []
        for n in arr:
            index = bisect.bisect_left(temp, n)
            if index == len(temp):
                temp.append(n)
            else:
                temp[index] = n
            print(f"The temp is: {temp}")
        return temp

    def longest_common_subsequence(self, a: str, b: str) -> int:
        lengths = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                if x == y:
                    lengths[i + 1][j + 1] = lengths[i][j] + 1
                else:
                    lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

        result = []
        x, y = len(a), len(b)

        while x != 0 and y != 0:
            if lengths[x][y] == lengths[x - 1][y]:
                x -= 1
            elif lengths[x][y] == lengths[x][y - 1]:
                y -= 1
            else:
                result.append(a[x - 1])
                x -= 1
                y -= 1

        return len(result)
