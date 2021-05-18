"""
To find the first occurrence of substring ~ using Robin Karp
Solution Approach:

"""
p = 31
m = 10 ** 9 + 9


def compute_hash(s):
    n = len(s)

    power_mod = [1]
    for i in range(n):
        power_mod.append((power_mod[-1] * p) % m)

    hash_values = [0] * (n + 1)

    for i in range(n):
        hash_values[i + 1] = (hash_values[i] + (ord(s[i]) - ord('a') + 1) * power_mod[i]) % m


def count_occurences(text, pattern):
    """
    :param pattern: Pattern Text
    :param text: I/P text
    :return:
    """
    text_length = len(text)
    pattern_length = len(pattern)

    power_mod = [1]
    for i in range(text_length):
        power_mod.append((power_mod[-1] * p) % m)
    # print(f"The power mod is: {[power_mod]}")

    hash_values = [0] * (text_length + 1)

    for i in range(text_length):
        hash_values[i + 1] = (hash_values[i] + (ord(text[i]) - ord('a') + 1) * power_mod[i]) % m
    # print("The string hash values are:", hash_values)

    pattern_hash = 0
    for i in range(pattern_length):
        pattern_hash += ((ord(pattern[i]) - ord('a') + 1) * power_mod[i]) % m
    # print("The pattern hash is:", pattern_hash)

    occurences = []

    i = 0
    while i + pattern_length - 1 < text_length:
        field_hash = (hash_values[i + pattern_length] - hash_values[i] + m) % m
        if field_hash == pattern_hash * power_mod[i] % m:
            occurences.append(i)
        i += 1

    print(len(occurences))
    return occurences

if __name__ == '__main__':
    text = "GACGCCA"
    pattern = "CGC"
    result = count_occurences(text, pattern)
    print(f"The pattern occurs in the following indexes {result}")
    print(f"The number of occurences is: {len(result)}")