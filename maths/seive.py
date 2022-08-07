def sieve(n):
    prime = [1 for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p] == 1:
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = 0
        p += 1
    prime[0] = 0
    prime[1] = 0
    print(prime)


if __name__ == '__main__':
    sieve(10)