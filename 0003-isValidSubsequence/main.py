array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def isValidSubsequence(array:list, sequence:list) -> bool:
    if len(array) == 0 and len(sequence) == 0:
        return True
    
    if len(array) < len(sequence):
        return False
    
    root_sequence = 0
    for num in array:
        if root_sequence < len(sequence) and num == sequence[root_sequence]:
            root_sequence +=1
    return root_sequence == len(sequence)








def isValidSubsequence(array:list, sequence:list) -> bool:
    root_sequence = 0
    for num in array:
        if root_sequence < len(sequence) and num == sequence[root_sequence]:
            root_sequence +=1
    return root_sequence == len(sequence)


print(isValidSubsequence(array,sequence))
