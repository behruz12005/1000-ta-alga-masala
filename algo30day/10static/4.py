def remove_duplicates(s: str) -> str:
    list_dub = []
    
    for char in s:

        if not list_dub or char != list_dub[-1]:
            list_dub.append(char)
            continue
        
        list_dub.pop()

    return ''.join(list_dub)


print(remove_duplicates("azxxzy"))