def compute_hash(s):
    p = 53
    m = 10**9 + 9
    hash_value = 0
    pow = 1

    for c in s:
        hash_value = (hash_value + (ord(c) - ord("a") + 1) * pow) % m
        pow = (pow * p) % m
    return hash_value


def compute_hash_faster(s):
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
        hash_values[i + 1] = (
            hash_values[i] + (ord(s[i]) - ord("a") + 1) * power_mod[i]
        ) % m
    print("The hash values are:", hash_values)

    return hash_values[-1]


if __name__ == "__main__":
    s = "codeforces"
    result = compute_hash(s)
    print(result)

    # Calling compute_hash_faster
    compute_hash_faster(s)
