# Consider the following
A = [(2, 2), (-1, 1), (1, 1)]
"""
1. Here by default it's the ascending order
2. We give max priority to x[1]
3. If x[1] is the same then we give priority to x[0], but the '-' sign indicates the reverse order
"""
A = sorted(A, key=lambda x: (x[1], -x[0]) )
