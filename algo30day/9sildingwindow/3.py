def longest_unique(lst):
    R = 0
    lines = set()
    while R < len(lst):
        if lst[R] not in lines:
            lines.add(lst[R])
            R += 1
        else:
            lines.remove(lst[R])
    return len(lines)

print(longest_unique([1,2,3,3,3,3]))