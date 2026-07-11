def lst_two_point(lst)->list:
    start = 0
    end = len(lst)-1
    while start <= end:
        lst[start], lst[end] = lst[end], lst[start]
        start+=1
        end-=1

    return lst

print(lst_two_point([1,2,3,4,5]))
