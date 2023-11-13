def solve(s, x):
    n = len(s)
    for length in range(x, x + 1):
        for i in range(0, n - length + 1):
            sub_str = s[i : i + length]
            print(sub_str)


if __name__ == "__main__":
    s = "HelloWorld"
    solve(s, x=3)
