def sort_map_by_value(H):
    return {k: v for k, v in sorted(H.items(), key=lambda item: item[1])}  # by value

def sort_map_by_key(H):
    return {k: v for k, v in sorted(H.items(), key=lambda item: item[0])}  # by key

if __name__ == '__main__':
    H = {1: 50, 2: 25, 3: 45, 4: 100, 5: 10}
    print(sort_map_by_value(H))
    print(sort_map_by_key(H))
