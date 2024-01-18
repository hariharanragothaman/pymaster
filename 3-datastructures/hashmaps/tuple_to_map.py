def tuple_to_hashmap(t1, t2):
    return dict(zip(t1, t2))

if __name__ == '__main__':
    # Let's say we have 2 tuples - we need to convert it into a hashmap
    t1 = (1, 2, 3)
    t2 = (4, 5, 6)
    mapping = tuple_to_hashmap(t1, t2)
    print(mapping)
