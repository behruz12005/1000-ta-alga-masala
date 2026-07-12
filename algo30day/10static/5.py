def comp(s: str):
    notsymbol = "#"
    stack = []

    for char in s:
        if char != notsymbol    :
            stack.append(char)
            continue
        if stack:
            stack.pop()

    return stack

def backspace_compare(s: str, t: str) -> bool:
    return comp(s) == comp(t)




print(backspace_compare("a##c", "#a#c"))