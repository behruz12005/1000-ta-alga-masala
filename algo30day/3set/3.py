def two_list_have(a,b) -> list:
    a_set = set(a)
    uniques_lsit= []
    for i in b:
        if i in a_set:
            uniques_lsit.append(i)

    return uniques_lsit


print(two_list_have([1, 2, 3, 4],[3, 4, 5, 6]))


def two_set_have(a,b) -> set:
    return set(a) - set(b)

print(two_set_have([1, 2, 3, 4],[3, 4, 5, 6]))
