from difflib import SequenceMatcher

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

def longest_common_substring(A, B):
    if set(A).isdisjoint(B):
        return 0
    a, b, size = SequenceMatcher(None, A, B, autojunk=False).find_longest_match(0, len(A), 0, len(B))
    return size

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


if __name__ == '__main__':
    s = "Success"
