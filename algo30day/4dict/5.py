
def word_dict(text):
    text_dict = {}
    
    for i in text:
        if i in text_dict:
            text_dict[i] +=1
        else:
            text_dict[i] = 1
    return text_dict

def first_unique(s):
    tengmi = word_dict(s)
    print(tengmi)
    for k,v in enumerate(s):
        if tengmi[v] == 1:
            return k

    return -1


print(first_unique("leetcode"))