def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) >> 1
    left, right = A[:mid], A[mid:]

    # Recursive call on each half
    merge_sort(left)
    merge_sort(right)

    # Two iterators for traversing the two halves
    i = 0
    j = 0

    # Iterator for the main list
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # The value from the left half has been used
            A[k] = left[i]
            # Move the iterator forward
            i += 1
        else:
            A[k] = right[j]
            j += 1
        # Move to the next slot
        k += 1

    # For all the remaining values
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k]=right[j]
        j += 1
        k += 1

    return A
