def list_to_dub(lst)->list:
    set_list = set()
    result = []

    for value in lst:
        if value not in set_list:
            set_list.add(value)
            result.append(value)

    return result

print(list_to_dub([1,2,2,4,3,23,2,32,23,23,2,32,3,1,2,1,23123,1]))
