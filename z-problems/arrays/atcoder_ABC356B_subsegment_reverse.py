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

def solve() -> None:
    n, l, r = input_as_array()
    A = list(range(0, n + 1))
    A = A[:l] + A[l:r + 1][::-1] + A[r + 1:]
    print(*A[1:])


# endregion

# region testcase
def main() -> None:
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    start_time = time.time()
    testcases = 1

    for i in range(testcases):
        solve()
        debug('-')

    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()


# endregion

# region debug

def input_as_array() -> list[int]:
    return list(map(int, input().split()))


def debug(char) -> None:
    if os.path.exists("data.in"):
        print(char * 25)


def debug2(value) -> None:
    if os.path.exists("data.in"):
        print(value)


# endregion


if __name__ == "__main__":
    main()
