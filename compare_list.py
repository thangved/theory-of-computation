import itertools


def to_string_list(a=[]):
    return itertools.permutations(a, len(a))


def to_string(tp=()):
    _str = ''
    for i in range(len(tp)):
        _str += tp[i]

    return _str


def compare(a=[], b=[]):
    list_a = to_string_list(a)
    list_b = to_string_list(b)

    for el_a in list_a:
        for el_b in list_b:
            if to_string(el_a) == to_string(el_b):
                return [el_a, el_b]

    return []


print(compare(['110', '0011', '0110'], ['110110', '00', '110']))
