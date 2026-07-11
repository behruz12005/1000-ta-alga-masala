def my_dub(lst):
    renum = set()
    for i in lst:
        if i not in renum:
            renum.add(i)
        else:
            return True
    return False


print(my_dub([]))
