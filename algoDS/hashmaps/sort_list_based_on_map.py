def sort_list_based_on_map(A, H):
    result = sorted(A, key=lambda x: H[x], reverse=True)
    return result

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    hmap = {1: 50, 2: 25, 3: 45, 4: 100, 5: 10}
    ans = sort_list_based_on_map(arr, hmap)
    print(ans)
