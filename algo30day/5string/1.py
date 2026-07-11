def palindrom(text):
    return text == text[::-1]

print(palindrom("radar")) 
print(palindrom("python")) 

def palindrom(text):
    start = 0
    end = len(text)-1
    while start < end:
        if text[start] != text[end]:
            return False
        start +=1
        end -=1
    return True
print(palindrom("alllla")) 
