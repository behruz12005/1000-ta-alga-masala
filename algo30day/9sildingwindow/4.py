def longest_unique(lst):
    L = 0
    R = 0
    window_set = set()
    max_len = 0
    while R < len(lst):
        if lst[R] not in window_set:
            window_set.add(lst[R])
            R+=1
            max_len = max(max_len,R-L)
        else:
            window_set.remove(lst[L])
            L+=1
    return lst[L:R]

print(longest_unique("123245"))