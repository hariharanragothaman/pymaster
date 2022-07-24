def solve(n, t):
    if n == 1 and 2 <= t <= 9:
        print(t)
    elif t == 1:
        print("1" * n)
    elif t == 2:
        # Last digit is 2
        print("1" * (n - 1) + "2")
    elif t == 10:
        # last Digit is zero
        ans = "1" * (n - 1) + "0"
        if ans == "0":
            print(-1)
        else:
            print(ans)
    elif t == 4:
        # Last 2 digits is divisible by 4
        print("1" * (n - 2) + "24")
    elif t == 3:
        # Sum of digits is divisible by 3
        print("3" * n)
    elif t == 8:
        # If the hundreds digit is even, the number formed by the last two digits must be divisible by 8.
        ans = (n - 2) * "2" + "16"
        print(ans)
    elif t == 9:
        # Sum is divisible by 9
        print("9" * n)
    elif t == 6:
        print("1" + (n - 2) * "0" + "2")
    elif t == 7:
        # number has 7 in it
        print(n * "7")
    elif t == 5:
        # Last digit is 5 / 0
        print("1" * (n - 1) + "5")