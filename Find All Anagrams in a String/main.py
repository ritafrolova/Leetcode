def func(s,p):
    l=len(p)
    splitted_by_pairs=[s[i:i+l] for i in range(0,len(s),l)]
    #print(splitted_by_pairs)
    for sym in splitted_by_pairs:
        #print(s.index(sym))
        if sorted(sym)==sorted(p):
            answer=True
            print(s.index(sym))
        else:
            answer=False
        
print(func("cbaebabacd","abc")) # работает
print(func("abab","ab")) # не работает
