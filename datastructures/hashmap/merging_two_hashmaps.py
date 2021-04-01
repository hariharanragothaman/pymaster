import collections
from collections import abc


def merge_hmaps(dct, merge_dct, add_keys=True):
    """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.

    This version will return a copy of the dictionary and leave the original
    arguments untouched.

    The optional argument ``add_keys``, determines whether keys which are
    present in ``merge_dict`` but not ``dct`` should be included in the
    new dict.

    Args:
        dct (dict) onto which the merge is executed
        merge_dct (dict): dct merged into dct
        add_keys (bool): whether to add new keys

    Returns:
        dict: updated dict
    """
    dct = dct.copy()
    if not add_keys:
        merge_dct = {
            k: merge_dct[k]
            for k in set(dct).intersection(set(merge_dct))
        }

    for k, v in merge_dct.items():
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.abc.Mapping)):
            dct[k] = merge_hmaps(dct[k], merge_dct[k], add_keys=add_keys)
        else:
            dct[k] = merge_dct[k]
    print(" I am going to return?", dct)
    return dct

def test_merge_hmaps():
    a = {
        'a': 1,
        'b': {
            'b1': 8,
            'b2': 3},
    }

    b = {
        'a': 1,
        'b': {
            'b1': [4, 5, 7],
            'b4': 5,
        },
    }
    """
    assert merge_hmaps(a, b)['a'] == 1
    assert merge_hmaps(a, b)['b']['b2'] == 3
    assert merge_hmaps(a, b)['b']['b1'] == 4
    """
    print("------------After merging -------------")
    res = merge_hmaps(a, b, add_keys=True)
    print("The merged hashmap is:", res)

if __name__ == '__main__':
    test_merge_hmaps()
