def longest_unique(lst):
    L = 0
    max_len = 0
    wd_set = set()
    for R in range(len(lst)):
        while lst[R] in wd_set:
            wd_set.remove(lst[L])
            L +=1
        wd_set.add(lst[R])
        max_len = max(max_len,R-L)
    return max_len

print(longest_unique([1,2,3,2,4,5]))