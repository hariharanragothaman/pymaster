def dayOfYear(self, D: str) -> int:
    D = [int(c) for c in D.split('-')][::-1]
    print(D)
    H = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    # Check if it's a leap year
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    if is_leap_year(D[-1]):
        H[2] = 29

    days = 0
    for i in range(1, D[1]):
        days += H[i]
    days += D[0]

    return days
