from collections import Counter

def top_k_frequent_words(self, A: list[str], k: int) -> list[str]:
    """
    # Classic example of sort by value and then by key
    # Here -ve sign signifies that you want to order values in reverse (and) setting it as 1st priority
    # then the key - which is second priority
    """
    ctr = Counter(A)
    result = sorted(ctr, key=lambda x: (-ctr[x], x))
    return result[:k]
