def get_hamming_distance(a, b):
    x = a ^ b
    dist = 0
    while x > 0:
        dist += x & 1
        x >>= 1
    return dist
