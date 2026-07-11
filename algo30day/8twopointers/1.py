def two_sum(lst,target)->list:
    start = 0
    end = len(lst)-1
    while start < end:
        print(lst[start] , lst[end])
        if lst[start] + lst[end] == target:
            return start,end
        elif lst[start] + lst[end] > target:
            end-=1
        elif lst[start] + lst[end] < target:
            start+=1

print(two_sum([1,2,3,4,5,6,9],9))