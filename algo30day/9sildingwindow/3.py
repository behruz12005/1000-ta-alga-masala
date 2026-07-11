def longest_unique(lst):
    L = 0
    R = 0
    window = set()
    max_len = 0
    while R < len(lst):
        if lst[R] not in window:
            window.add(lst[R])
            R +=1
            max_len = max(max_len, R - L)
        else:
            window.remove(lst[L])
            L +=1
    return max_len



print(longest_unique([1,2,3,2,4]))