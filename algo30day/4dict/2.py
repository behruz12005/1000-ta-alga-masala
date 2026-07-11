from collections import Counter

resu = Counter([1,2,3,4,4,5,2,2,3,1])

print(resu)
def word_dict(text):
    text_dict = {}
    
    for i in text:
        if i in text_dict:
            text_dict[i] +=1
        else:
            text_dict[i] = 1
    return text_dict

print(word_dict("anna"))
