def has_number_linear(lst,target):
    for i in lst:
        if i == target:
            return True
        
    return False

# print(has_number_linear([1,3,4,5,65,6,3,1],34))


def has_number_set(lst,target):

    return target in set(lst)

print(has_number_set([1,3,4,5,65,6,3,1],4))


