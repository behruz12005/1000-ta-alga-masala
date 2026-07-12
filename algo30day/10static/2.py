def is_valid(s: str) -> bool:
    brackets = {
        "}": "{",
        ")": "(",
        "]": "[",
    }
    stack = []

    for char in s:
        if char not in brackets:
            stack.append(char)
        elif not stack:
            return False
        else:
            last_stack = stack.pop()
            if last_stack != brackets[char]:
                return False
        
        
    return not stack


text = '}[]{}'
print(is_valid(text))
        

