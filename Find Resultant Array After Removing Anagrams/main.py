def func(words):
    list_sorted=[]
    for word in words:
        sorted_word=sorted(word)
        list_sorted.append(sorted_word)
    result_list=[]
    for _ in list_sorted:
        if _ not in result_list:
            result_list.append(_)
    return result_list
print(func(["abba","baba","bbaa","cd","cd"]))   #["abba","cd"]