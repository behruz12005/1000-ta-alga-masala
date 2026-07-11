def silding_window(lst,k) -> int:
    start_w = 1
    end_w = k
    max = sum([lst[i] for i in range(k)])
    result_max = max
    while end_w < len(lst):
        max = (max - lst[start_w-1])+lst[end_w]
        if result_max < max:
            result_max = max
        start_w+=1
        end_w+=1
    return result_max
print(silding_window([-4, -2, -7, -1], 2))
