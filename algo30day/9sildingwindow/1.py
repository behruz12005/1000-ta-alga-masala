def silding_window(lst,k) -> int:
    start_w = 0
    end_w = k
    max = 0
    while end_w <= len(lst):
        max_value = 0
        for i in range(start_w,end_w):
            max_value+=lst[i]

        if max < max_value:
            max = max_value
        start_w+=1
        end_w+=1

    return max
print(silding_window([1,2,3,4,5,6,7],3))

            