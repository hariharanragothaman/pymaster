"""
செயல் பேசும் ஆழம் இங்கே சொற்கள் பேசுமா?

Focus, Determination and Sheer-Will

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
"""

# region imports

import os, sys, math, cmath, time, collections

# endregion

# region solution

"""
# This solution came to my mind, naturally top-down

def solve() -> None:
    num = int(input())
    # print(num)
    S = list(range(1, 7))
    S = [c for c in S if c <= num]
    # print(S)

    cnt = 0

    A = []

    def helper(start):
        # print(f"The start is: {start} and cnt is: {cnt}")
        if start == num:
            A.append(1)
            # print(f"We have reached the leaf..{cnt}")
            return
        else:
            # print(f"Entering else block")
            ans = 0
            for c in S:
                val = start + c
                if val <= num:
                    # print(f"The val is: {val}")
                    helper(val)

    helper(0)
    print(sum(A) % MOD)
"""

"""

# This solution, computes in reverse, and we store a memo{}
def solve() -> None:
    num = int(input())
    S = list(range(1, 7))

    # Initialize a memoization dictionary to store computed values
    memo = {}

    def helper(current_num):
        if current_num == 0:
            return 1
        if current_num < 0:
            return 0
        if current_num in memo:
            return memo[current_num]

        ways = 0
        for c in S:
            ways += helper(current_num - c)

        # Cache the result for this current_num
        memo[current_num] = ways
        return ways

    result = helper(num)
    print(result % MOD)
"""

"""
# This one does the same thing as above, stores a better map
def solve() -> None:
    num = int(input())
    S = list(range(1, 7))

    # Initialize a memoization dictionary to store computed values

    limit = 10**6 + 1
    DP = [0] * limit
    DP[0] = 1

    def helper(current_num):
        # print(f"The current_num is: {current_num}")
        if DP[current_num] != 0:
            return DP[current_num]

        for c in S:
            if current_num - c >= 0:
                # print(f"{current_num} calling DP({current_num-c})")
                DP[current_num] += helper(current_num-c)

        return DP[current_num]

    # print(DP)
    result = helper(num)
    # print(DP)
    print(result % MOD)
"""

MOD = 10 ** 9 + 7


# So Top-Down can fail and bottom-up only works here in CSES?
def solve():
    n = int(input())
    DP = [0] * (n + 1)
    DP[0] = 1

    for i in range(1, n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                DP[i] += DP[i - j]

    print(DP[n] % MOD)


# endregion

# region testcase
def main() -> None:
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    start_time = time.time()

    # testcases = int(input())
    testcases = 1

    for i in range(testcases):
        solve()
        # debug('-')

    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()


# endregion


if __name__ == "__main__":
    main()
