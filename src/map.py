from collections import Counter


class Map:
    def sort_by_value(self, H):
        return {k:v for k, v in sorted(H.items(), key= lambda item: item[1])}

    def sort_by_key(self, H):
        return {k:v for k, v in sorted(H.items(), key= lambda item: item[0])}

    def sort_by_value_then_key(self, H: dict) -> list:
        """
        To sort by value and then by key
        Creates a tuple that are by default sorted by value, and then we set the priority
        """
        ans = sorted(H, key=lambda x: (-H[x], x))
        return ans

    def sort_map_by_priority(self, H: dict) -> list:
        A = [(k, v) for k, v in H.items()]
        A = sorted(A, key=lambda x: (x[1], -x[0]))
        return A

    def top_k_frequent_words(self, A: list[str], k: int) -> list[str]:
        """
        Classic example of sort by value and then by key
        Here -ve sign signifies that you want to order values in reverse (and) setting it as 1st priority
        then the key - which is second priority
        """
        ctr = Counter(A)
        result = sorted(ctr, key=lambda x: (-ctr[x], x))
        return result[:k]

    def tuple_to_map(self, t1, t2):
        return dict(zip(t1, t2))

    def sort_list_based_on_map(self, A, H):
        result = sorted(A, key=lambda x: H[x], reverse=True)
        return result

    def most_common_in_array(self, A):
        ctr = Counter(A)
        top_three_frequent = ctr.most_common(3)
        return  top_three_frequent
