"""
delete duplicates in sorted array, and shift elements to the left
"""

# There is several ways to do this easily with additional space
# We are trying to do it, with less space as possible

from typing import List


def delete_duplicates(arr: List[int]) -> int:
    """
    Return the number of valid entries after deletion
    Args:
        arr:
    Returns: number of entries
    """
    if not arr:
        return 0

    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            cnt += 1
    print(f"The total count is: {cnt}")


def delete_duplicates_updated(arr: List[int]) -> List[int]:
    if not arr:
        return []

    write_index = 1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    print(f"The new length is: {write_index}")
    print(f"The array is: {arr}")


if __name__ == "__main__":
    arr = [2, 3, 5, 5, 7, 11, 11, 11, 15]
    delete_duplicates(arr)
    delete_duplicates_updated(arr)
