def word_dict(text):
    dict_text = {}
    for i in text:
        if i not in dict_text:
            dict_text[i] =1
        else:
            dict_text[i] +=1
    return dict_text

def anagram(t1,t2):
    return word_dict(t1) == word_dict(t2)

print(anagram("allo", "allo"))