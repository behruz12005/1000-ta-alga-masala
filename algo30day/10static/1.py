def reverse_string(s: str) -> str:
    list_s = list(s)
    strin_re = []
    while list_s:
        strin_re.append(list_s.pop())
    return "".join(strin_re)
print(reverse_string("salom"))
