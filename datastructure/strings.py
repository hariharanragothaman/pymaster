import bisect
import itertools

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

    def check_anagrams_version2(self, str1, str2):
        hmap1 = [0] * 26
        hmap2 = [0] * 26

        for char in str1:
            pos = ord(char) - ord("a")
            hmap1[pos] += 1

        for char in str2:
            pos = ord(char) - ord("a")
            hmap2[pos] += 1

        return hmap1 == hmap2

    def find_first_index(self, a, target):
        idx = a.find(target)
        return idx

    def find_between_two_indexes(self, a, target, low, high):
        idx = a.find(target, low, high)
        return idx

    # returns the highest index
    def find_highest_index(self, a, target):
        idx = a.rfind(target, 0, len(a))
        return idx


class SplitStrings:
    def split_into_same_char_segments(s):
        n, ans, ch = len(s), [], ""

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                ch += s[i]
            elif s[i] != s[i + 1]:
                ch += s[i]
                ans.append(ch)
                ch = ""
        if ch:
            ch += s[-1]
            ans.append(ch)
        else:
            ans.append(s[-1])
        return ans


    def split_into_same_char_segments_2(s):
        groups= []
        for _, v in itertools.groupby(s):
            groups.append(''.join(v))
        return groups

    def split_into_same_char_segments_3(arr):
        """
        This helps in splitting the array and finding continuous subsegments smartly
        """
        temp = []
        n = len(arr)

        cnt, prev = 1, arr[0]
        for i in range(n - 1):
            if arr[i + 1] == prev:
                cnt += 1
            else:
                temp.append(cnt)
                cnt = 1
            prev = arr[i + 1]
        temp.append(cnt)
        return temp

class Substrings:
    def generate_all_substring(s):
        ans = []
        for left in range(len(s)):
            for right in range(left, len(s)):
                substring = s[left : right + 1]
                ans.append(substring)
        return ans

    def generate_x_length_substring(s, x):
        ans = []
        n = len(s)
        for length in range(x, x + 1):
            for i in range(0, n - length + 1):
                sub_str = s[i : i + length]
                ans.append(sub_str)
        return ans

    def check_for_common_substring(s1, s2):
        return "YES" if set(list(s1)) & set(list(s2)) != set() else "NO"

    def find_longest_substring_length_of_char(s, char):
        n = len(s)
        max_count = 0
        tmp = 0
        for i in range(0, n):
            if s[i] == char:
                tmp += 1
            else:
                max_count = max(max_count, tmp)
                tmp = 0
        max_count = max(max_count, tmp)
        return max_count


    def longest_common_substring(A, B):
        if set(A).isdisjoint(B):
            return 0
        a, b, size = SequenceMatcher(None, A, B, autojunk=False).find_longest_match(0, len(A), 0, len(B))
        return size

    def count_substrings_anagrams(s):
        ctr = Counter()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sl = tuple(sorted(s[i:j]))
                ctr[sl] = ctr.get(sl, 0) + 1

        result = 0
        for k, v in ctr.items():
            result += (v * (v - 1)) // 2
        return result

    def count_distinct_substrings(s):
        n = len(s)
        p = 53
        m = 10**9 + 9

        # Pre-computing the powers of 31
        power_mod = [1]
        for i in range(1, n):
            power_mod.append((power_mod[-1] * p) % m)

        # Basically doing hash-values in prefix sum
        hash_values = [0] * (n + 1)
        for i in range(n):
            hash_values[i + 1] = (hash_values[i] + (ord(s[i]) - ord("a") + 1) * power_mod[i]) % m
        print("The hash-values are:", hash_values)

        # Actual solution starts here
        count = 0
        n = len(s)
        for length in range(1, n + 1):
            result_set = set()
            for i in range(0, n - length + 1):
                string = s[i : i + length]
                # print("The value of length ",length, i)
                print("The string is:", string)
                current_hash = (hash_values[i + length] + m - hash_values[i]) % m
                current_hash = (current_hash * power_mod[n - i - length]) % m
                result_set.add(current_hash)

            print(f"The result is: {result_set}")
            count += len(result_set)
        print("The number of unique substrings is:", count)
        return count

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
