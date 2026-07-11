def remove_element(lst,val) -> int:
    k = 0
    for i in range(len(lst)):     # i = o'qish belgisi
        if lst[i] != val:          # yaxshi element topildi
            lst[k] = lst[i]        # uni yozish joyiga qo'y
            k += 1 

    return lst,k

print(remove_element([3,2,2,3,2,3,4,3],3))
