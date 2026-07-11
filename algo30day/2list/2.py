def max_min(lst):
    if len(lst) == 0:      
        return None
    eng_katta = lst[0]         
    eng_kichik = lst[0]         
    for son in lst:
        if son > eng_katta:
            eng_katta = son
        if son < eng_kichik:
            eng_kichik = son
    return [eng_katta, eng_kichik]

print(max_min([3, 7, 1, 9, 4]))