def two_sum(lst,target):
    ayrma_dict = {}
    for key,value in enumerate(lst):
        ayrma = target-value
        if ayrma in ayrma_dict:
            return [ayrma_dict[ayrma],key]
            # return [lst[ayrma_dict[value]],lst[key]]

        ayrma_dict[value] = key

print(two_sum([2,4,5,1],9))
        