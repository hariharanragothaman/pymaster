def compute_hash(s):
    p = 31
    m = 10**9 + 9
    hash_value = 0
    pow = 1

    for c in s:
        hash_value = (hash_value + (ord(c) - ord('a') + 1) * pow ) % m
        pow = (pow * p) % m
    return hash_value

if __name__ == '__main__':
    s = 'codeforces'
    result = compute_hash(s)
    print(result)