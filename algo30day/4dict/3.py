def word_dict(text):
    text_dict = {}
    
    for i in text:
        if i in text_dict:
            text_dict[i] +=1
        else:
            text_dict[i] = 1
    return text_dict


def is_anagram(s1, s2):
    return word_dict(s1) == word_dict(s2)

from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)


print(is_anagram("rat","car"))
    