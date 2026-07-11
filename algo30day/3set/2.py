def noyob_value(lst)-> list:
    noyob_set = set()
    for i in lst:
        if i not in noyob_set:
            noyob_set.add(i)

    return noyob_set

print(noyob_value([1, 3, 3, 5, 1] ))


def noyob_value(lst)-> list:
    return set(lst)

print(noyob_value([1, 3, 3, 5, 1] ))

def noyob_lem(lst)-> int:
    return len(set(lst))

print(noyob_lem([1, 3, 3, 5, 1] ))
